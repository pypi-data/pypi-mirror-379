#!/usr/bin/env python
"""Benchmark using Apache Bench (ab) - tests servers sequentially to avoid performance impact."""

import subprocess
import re
import statistics
import time
import signal
import sys
import os
import json
from datetime import datetime
from typing import Dict, Any, List

try:
    from tabulate import tabulate
    HAS_TABULATE = True
except ImportError:
    HAS_TABULATE = False
    print("Warning: tabulate not installed. Install with: pip install tabulate")
    print("Using basic formatting instead.\n")

# Single port used for both servers (tested sequentially)
PORT = 8001
BASE_URL = f"http://127.0.0.1:{PORT}"

# Number of requests and concurrency
REQUESTS = 1000
CONCURRENCY = 10

def run_ab_test(url: str, method: str = 'GET', post_data: str = None) -> Dict[str, Any] | None:
    """Run Apache Bench test and parse results."""
    try:
        cmd = [
            'ab',
            '-n', str(REQUESTS),
            '-c', str(CONCURRENCY),
            '-q',  # Quiet mode
            url
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30, input=post_data if post_data else None)
        
        if result.returncode != 0:
            return None
        
        output = result.stdout
        
        # Parse key metrics from ab output
        metrics = {}
        
        # Time per request (mean)
        match = re.search(r'Time per request:\s+([\d.]+)\s+\[ms\]\s+\(mean\)', output)
        if match:
            metrics['mean'] = float(match.group(1))

        # Connection times (min, mean, median, max)
        match = re.search(r'Total:\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)\s+([\d.]+)', output)
        if match:
            metrics['min'] = float(match.group(1))
            metrics['mean_conn'] = float(match.group(2))
            metrics['median'] = float(match.group(3))
            metrics['max'] = float(match.group(4))
        
        # Requests per second
        match = re.search(r'Requests per second:\s+([\d.]+)', output)
        if match:
            metrics['rps'] = float(match.group(1))
        
        # Transfer rate
        match = re.search(r'Transfer rate:\s+([\d.]+)', output)
        if match:
            metrics['transfer_rate'] = float(match.group(1))
        
        # Percentage times
        percentiles = {}
        for line in output.split('\n'):
            if '%' in line and 'served within' not in line:
                parts = line.strip().split()
                if len(parts) >= 2:
                    try:
                        percent = int(parts[0].replace('%', ''))
                        time_ms = float(parts[1])
                        percentiles[f'p{percent}'] = time_ms
                    except:
                        continue

        metrics.update(percentiles)
        return metrics
        
    except subprocess.TimeoutExpired:
        print(f"Timeout testing {url}")
        return None
    except FileNotFoundError:
        print("Apache Bench (ab) not found. Please install it:")
        print("  Ubuntu/Debian: sudo apt-get install apache2-utils")
        print("  macOS: brew install httpd")
        print("  Fedora/RHEL: sudo dnf install httpd-tools")
        return None
    except Exception as e:
        print(f"Error testing {url}: {e}")
        return None

def format_number(n: float) -> str:
    """Format number with appropriate precision."""
    if n >= 1000:
        return f"{n:.0f}"
    elif n >= 10:
        return f"{n:.1f}"
    else:
        return f"{n:.2f}"

def start_server(server_type: str) -> subprocess.Popen | None:
    """Start a server and return the process."""
    try:
        if server_type == 'django':
            # Start Django server using ASGI application
            cmd = ['python', '-c', f'''
import sys
sys.path.insert(0, "..")
from benchmark.django_app.asgi import application
import uvicorn
uvicorn.run(application, host="127.0.0.1", port={PORT}, log_level="error")
''']
            print(f"  Starting Django server on port {PORT}...")
        else:
            # Modify FastAPI to use the same port
            cmd = ['python', '-c', f'''
import sys
sys.path.insert(0, "..")
from benchmark.fastapi_app import app
import uvicorn
uvicorn.run(app, host="127.0.0.1", port={PORT}, log_level="error")
''']
            print(f"  Starting FastAPI server on port {PORT}...")
        
        process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT, text=True)
        time.sleep(3)  # Give server time to start

        # Check if server is responding
        test_url = f"{BASE_URL}/users/?count=1"
        result = subprocess.run(['curl', '-s', '-o', '/dev/null', '-w', '%{http_code}', test_url],
                              capture_output=True, text=True, timeout=10)
        if result.stdout == '200':
            print(f"    ✓ Server started successfully")
            return process
        else:
            print(f"    ✗ Server failed to start (HTTP {result.stdout})")
            # Get server output regardless of whether it's still running
            try:
                stdout, stderr = process.communicate(timeout=2)
                print(f"    Server stdout: {stdout}")
                print(f"    Server stderr: {stderr}")
            except subprocess.TimeoutExpired:
                if process.poll() is None:
                    print("    Server is still running but not responding")
                    # Try to get logs from a running server
                    try:
                        test_url_error = f"{BASE_URL}/users/?count=1"
                        error_result = subprocess.run(['curl', '-s', test_url_error],
                                                    capture_output=True, text=True, timeout=5)
                        print(f"    Server response: {error_result.stdout}")
                        print(f"    Server error response: {error_result.stderr}")
                    except Exception as e:
                        print(f"    Could not get server response: {e}")
                else:
                    print(f"    Server exited with code {process.returncode}")
            process.terminate()
            return None
            
    except Exception as e:
        print(f"    ✗ Error starting server: {e}")
        return None

def stop_server(process: subprocess.Popen):
    """Stop a server process."""
    if process:
        process.terminate()
        try:
            process.wait(timeout=2)
        except:
            process.kill()
        print("    ✓ Server stopped")

def print_table(data: List[List[str]], headers: List[str], title: str = None):
    """Print a formatted table."""
    if title:
        print(f"\n{title}")
        print("-" * 80)

    if HAS_TABULATE:
        print(tabulate(data, headers=headers, tablefmt='fancy_grid'))
    else:
        # Basic formatting without tabulate
        col_widths = []
        for i in range(len(headers)):
            max_width = len(headers[i])
            for row in data:
                if i < len(row):
                    max_width = max(max_width, len(str(row[i])))
            col_widths.append(max_width + 2)

        # Print headers
        header_line = ""
        for i, header in enumerate(headers):
            header_line += str(header).ljust(col_widths[i])
        print(header_line)
        print("-" * sum(col_widths))

        # Print data
        for row in data:
            row_line = ""
            for i, cell in enumerate(row):
                if i < len(col_widths):
                    row_line += str(cell).ljust(col_widths[i])
            print(row_line)

def write_results_to_file(django_results: Dict[str, Dict[str, Any]], fastapi_results: Dict[str, Dict[str, Any]], comparison_data: List[List[str]], summary_data: List[List[str]], throughput_info: str = None):
    """Write benchmark results to a timestamped file in formatted table format."""
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"benchmark_results_{timestamp}.txt"

    try:
        with open(filename, 'w') as f:
            # Header
            f.write("="*80 + "\n")
            f.write("🚀 django-rapid vs FASTAPI: COMPREHENSIVE PERFORMANCE COMPARISON\n")
            f.write("   Benchmarking Django with django-rapid (@validate) decorator vs FastAPI\n")
            f.write("   Including serialization, validation, and plain JSON endpoints\n")
            f.write("="*80 + "\n\n")

            # Configuration
            f.write("📋 BENCHMARK CONFIGURATION\n")
            f.write("-"*50 + "\n")
            f.write(f"Timestamp: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            f.write(f"Requests: {REQUESTS}\n")
            f.write(f"Concurrency: {CONCURRENCY}\n")
            f.write(f"Port: {PORT}\n\n")

            # Django Results
            f.write("📦 DJANGO+MSGSPEC DETAILED RESULTS\n")
            f.write("-"*50 + "\n")

            django_table = []
            for name in sorted(django_results.keys()):
                stats = django_results[name]
                django_table.append([
                    name,
                    f"{stats['mean']:.2f}ms",
                    f"{stats.get('rps', 0):.1f}",
                    f"{stats['min']:.1f}ms",
                    f"{stats['median']:.1f}ms",
                    f"{stats['max']:.1f}ms",
                    f"{stats.get('transfer_rate', 0):.1f} KB/s"
                ])

            if django_table:
                headers = ['Endpoint', 'Mean Time', 'RPS', 'Min', 'Median', 'Max', 'Transfer Rate']
                f.write(tabulate(django_table, headers=headers, tablefmt='grid') + "\n\n")

            # FastAPI Results
            f.write("📦 FASTAPI DETAILED RESULTS\n")
            f.write("-"*50 + "\n")

            fastapi_table = []
            for name in sorted(fastapi_results.keys()):
                stats = fastapi_results[name]
                fastapi_table.append([
                    name,
                    f"{stats['mean']:.2f}ms",
                    f"{stats.get('rps', 0):.1f}",
                    f"{stats['min']:.1f}ms",
                    f"{stats['median']:.1f}ms",
                    f"{stats['max']:.1f}ms",
                    f"{stats.get('transfer_rate', 0):.1f} KB/s"
                ])

            if fastapi_table:
                headers = ['Endpoint', 'Mean Time', 'RPS', 'Min', 'Median', 'Max', 'Transfer Rate']
                f.write(tabulate(fastapi_table, headers=headers, tablefmt='grid') + "\n\n")

            # Comparison Table
            if comparison_data:
                f.write("📊 DETAILED COMPARISON RESULTS\n")
                f.write("-"*50 + "\n")
                headers = ['Endpoint', 'Django+msgspec', 'FastAPI', 'Winner', 'Speed Diff']
                f.write(tabulate(comparison_data, headers=headers, tablefmt='grid') + "\n\n")

            # Reference Results
            reference_data = []
            for name in django_results:
                if name not in fastapi_results:
                    continue
                if "(Plain)" in name or "(Direct)" in name:
                    django_stats = django_results[name]
                    fastapi_stats = fastapi_results[name]
                    reference_data.append([
                        name,
                        f"{django_stats['mean']:.2f}ms",
                        f"{fastapi_stats['mean']:.2f}ms",
                        f"{fastapi_stats['mean']/django_stats['mean']:.2f}x" if django_stats['mean'] > 0 else "N/A"
                    ])

            if reference_data:
                f.write("📋 REFERENCE RESULTS (Plain/Direct Endpoints)\n")
                f.write("-"*50 + "\n")
                headers = ['Endpoint', 'Django', 'FastAPI', 'FastAPI Factor']
                f.write(tabulate(reference_data, headers=headers, tablefmt='grid') + "\n\n")

            # Summary Table
            if summary_data:
                f.write("🏆 FINAL SUMMARY\n")
                f.write("-"*50 + "\n")
                headers = ['Category', 'Django Avg', 'FastAPI Avg', 'Speed Factor', 'Winner']
                f.write(tabulate(summary_data, headers=headers, tablefmt='grid') + "\n\n")

            # Throughput Info
            if throughput_info:
                f.write("🚀 THROUGHPUT COMPARISON\n")
                f.write("-"*50 + "\n")
                f.write(f"{throughput_info}\n\n")

            # Footer
            f.write("="*80 + "\n")
            f.write("Benchmark completed successfully!\n")
            f.write("="*80 + "\n")

        print(f"\n💾 Results written to: {filename}")
    except Exception as e:
        print(f"Error writing results to file: {e}")

def run_benchmark():
    """Run the benchmark comparison - testing servers sequentially."""
    endpoints = [
        # Pure serialization test - where our msgspec optimizations shine!
        ('/large-dict/?size=100', 'Large Dict (100)', 'GET', None),
        ('/large-dict/?size=1000', 'Large Dict (1000)', 'GET', None),

        # Real-world Django ORM vs SQLAlchemy endpoints
        ('/users/?limit=100', '100 Users (DB)', 'GET', None),
        ('/users/?limit=1000', '1000 Users (DB)', 'GET', None),
        ('/posts/?limit=100', '100 Posts (DB)', 'GET', None),
        ('/posts/?limit=1000', '1000 Posts (DB)', 'GET', None),
        ('/create-user/', 'Create User (POST)', 'POST', '{"name": "Test User", "email": "test@example.com", "age": 25}'),
        ('/search-users/?q=test&limit=50', 'Search Users', 'GET', None),
        ('/dashboard/', 'Dashboard Stats', 'GET', None),

        # Reference endpoints for comparison (not included in main comparison)
        ('/users-plain/?limit=100', '100 Users (Plain)', 'GET', None),
        ('/users-msgspec-direct/?limit=100', '100 Users (Direct)', 'GET', None),
    ]
    
    print("\n" + "="*80)
    print("🚀 django-rapid vs FASTAPI: COMPREHENSIVE PERFORMANCE COMPARISON")
    print("   Benchmarking Django with django-rapid (@validate) decorator vs FastAPI")
    print("   Including serialization, validation, and plain JSON endpoints")
    print(f"   Requests: {REQUESTS} | Concurrency: {CONCURRENCY} | Port: {PORT}")
    print("="*80)
    
    # Store results for each framework
    django_results = {}
    fastapi_results = {}
    
    # Test Django first
    print("\n" + "="*50)
    print("📦 TESTING DJANGO+MSGSPEC")
    print("="*50)
    
    django_process = start_server('django')
    if django_process:
        for endpoint_info in endpoints:
            path, name, method, post_data = endpoint_info
            print(f"\n  Testing endpoint: {name}")
            url = f"{BASE_URL}{path}"
            stats = run_ab_test(url, method, post_data)
            if stats:
                django_results[name] = stats
                print(f"    Mean: {format_number(stats['mean'])}ms | RPS: {format_number(stats.get('rps', 0))}")
        stop_server(django_process)
    else:
        print("  ❌ Could not start Django server")
        return
    
    # Cool down period
    print("\n  Waiting 5 seconds before testing next framework...")
    time.sleep(5)
    
    # Test FastAPI
    print("\n" + "="*50)
    print("📦 TESTING FASTAPI")
    print("="*50)
    
    fastapi_process = start_server('fastapi')
    if fastapi_process:
        for endpoint_info in endpoints:
            path, name, method, post_data = endpoint_info
            print(f"\n  Testing endpoint: {name}")
            url = f"{BASE_URL}{path}"
            stats = run_ab_test(url, method, post_data)
            if stats:
                fastapi_results[name] = stats
                print(f"    Mean: {format_number(stats['mean'])}ms | RPS: {format_number(stats.get('rps', 0))}")
        stop_server(fastapi_process)
    else:
        print("  ❌ Could not start FastAPI server")
        return
    
    # Compare results with better formatting
    print("\n" + "="*80)
    print("📊 DETAILED COMPARISON RESULTS")
    print("="*80)
    
    # Prepare comparison data
    comparison_data = []
    
    for name in django_results:
        if name not in fastapi_results:
            continue

        # Skip plain and direct endpoints from main comparison
        if "(Plain)" in name or "(Direct)" in name:
            continue

        django_stats = django_results[name]
        fastapi_stats = fastapi_results[name]
        
        django_mean = django_stats['mean']
        fastapi_mean = fastapi_stats['mean']

        # Determine winner (lower time is better)
        if django_mean < fastapi_mean:
            winner = "Django ✅"
            speed_diff = f"{fastapi_mean/django_mean:.2f}x"
        else:
            winner = "FastAPI ✅"
            speed_diff = f"{django_mean/fastapi_mean:.2f}x"
        
        comparison_data.append([
            name,
            f"{django_mean:.2f}ms",
            f"{fastapi_mean:.2f}ms",
            winner,
            speed_diff
        ])
    
    # Print main comparison table
    headers = ['Endpoint', 'Django+msgspec', 'FastAPI', 'Winner', 'Speed Diff']
    print_table(comparison_data, headers)
    
    # Group results by type
    print("\n" + "="*80)
    print("📈 PERFORMANCE BY ENDPOINT TYPE")
    print("="*80)
    
    # Analyze all endpoints (main comparison)
    msgspec_data = []
    for name in django_results:
        if name not in fastapi_results:
            continue

        # Skip plain and direct endpoints from main comparison
        if "(Plain)" in name or "(Direct)" in name:
            continue

        django_stats = django_results[name]
        fastapi_stats = fastapi_results[name]

        # Calculate speedup (lower time is better)
        django_time = django_stats['mean']
        fastapi_time = fastapi_stats['mean']

        if django_time < fastapi_time:
            factor = fastapi_time / django_time
            faster = "Django"
        else:
            factor = django_time / fastapi_time
            faster = "FastAPI"

        msgspec_data.append([
            name,
            f"{django_time:.2f}ms",
            f"{fastapi_time:.2f}ms",
            f"{factor:.2f}x",
            faster
        ])

    if msgspec_data:
        headers = ['Test', 'Django+msgspec', 'FastAPI', 'Factor', 'Faster']
        print_table(msgspec_data, headers, "🚀 django-rapid vs FastAPI Performance:")

    # Show plain and direct endpoints for reference
    print("\n" + "="*80)
    print("📋 REFERENCE RESULTS (not included in main comparison)")
    print("="*80)

    reference_data = []
    for name in django_results:
        if name not in fastapi_results:
            continue

        # Only include plain and direct endpoints
        if "(Plain)" not in name and "(Direct)" not in name:
            continue

        django_stats = django_results[name]
        fastapi_stats = fastapi_results[name]

        django_time = django_stats['mean']
        fastapi_time = fastapi_stats['mean']

        reference_data.append([
            name,
            f"{django_time:.2f}ms",
            f"{fastapi_time:.2f}ms",
            f"{fastapi_time/django_time:.2f}x" if django_time > 0 else "N/A"
        ])

    if reference_data:
        headers = ['Test', 'Django', 'FastAPI', 'FastAPI Factor']
        print_table(reference_data, headers, "📊 Plain/Direct Endpoints (Reference):")


    # Overall summary focused on django-rapid vs FastAPI
    if django_results and fastapi_results:
        print("\n" + "="*80)
        print("🏆 django-rapid vs FASTAPI: THE RESULTS")
        print("="*80)

        summary_data = []

        # Main comparison endpoints (excluding plain and direct)
        django_means = [django_results[k]['mean'] for k in django_results if "(Plain)" not in k and "(Direct)" not in k]
        fastapi_means = [fastapi_results[k]['mean'] for k in fastapi_results if k in django_results and "(Plain)" not in k and "(Direct)" not in k]
        if django_means and fastapi_means:
            django_avg = statistics.mean(django_means)
            fastapi_avg = statistics.mean(fastapi_means)

            # Calculate factor (lower time is better)
            if django_avg < fastapi_avg:
                factor = fastapi_avg / django_avg
                winner = "Django 🏆"
            else:
                factor = django_avg / fastapi_avg
                winner = "FastAPI 🏆"

            summary_data.append([
                "All Endpoints",
                f"{django_avg:.2f}ms",
                f"{fastapi_avg:.2f}ms",
                f"{factor:.2f}x",
                winner
            ])



        headers = ['Category', 'Django Avg', 'FastAPI Avg', 'Speed Factor', 'Winner']
        print_table(summary_data, headers)
        
        # Throughput comparison (excluding plain and direct endpoints)
        django_rps = [s['rps'] for k, s in django_results.items() if 'rps' in s and "(Plain)" not in k and "(Direct)" not in k]
        fastapi_rps = [s['rps'] for k, s in fastapi_results.items() if 'rps' in s and "(Plain)" not in k and "(Direct)" not in k]

        throughput_info = None
        if django_rps and fastapi_rps:
            django_avg_rps = statistics.mean(django_rps)
            fastapi_avg_rps = statistics.mean(fastapi_rps)
            rps_ratio = django_avg_rps / fastapi_avg_rps

            print(f"\n🚀 Throughput Comparison:")
            print(f"  Django+msgspec: {format_number(django_avg_rps)} req/s")
            print(f"  FastAPI:        {format_number(fastapi_avg_rps)} req/s")

            if rps_ratio > 1:
                throughput_info = f"Django handles {rps_ratio:.2f}x more requests/sec"
                print(f"  → {throughput_info}")
            else:
                rps_ratio_inv = 1/rps_ratio
                throughput_info = f"FastAPI handles {rps_ratio_inv:.2f}x more requests/sec"
                print(f"  → {throughput_info}")

        # Write results to file
        write_results_to_file(django_results, fastapi_results, comparison_data, summary_data, throughput_info)

if __name__ == '__main__':
    print("\n📝 SEQUENTIAL BENCHMARK")
    print("-"*50)
    print("This script will:")
    print("1. Start Django server and test all endpoints")
    print("2. Stop Django server")
    print("3. Start FastAPI server and test all endpoints")
    print("4. Stop FastAPI server")
    print("5. Compare results")
    print("\nThis ensures no performance interference between servers.")
    print("\nRequirements:")
    print("- Apache Bench (ab) installed")
    print("- Dependencies: pip install -r ../requirements-benchmark.txt")
    
    input("\nPress Enter to start sequential benchmark...")
    
    run_benchmark()
    print("\nBenchmark complete!")
