import pandas as pd
import glob
import time
import multiprocessing
import math

# -------------------------------
# CSV Processing Functions
# -------------------------------
def process_csv(file):
    df = pd.read_csv(file)
    mean_values = df.mean(numeric_only=True)
    max_values = df.max(numeric_only=True)
    min_values = df.min(numeric_only=True)

    result = {"file": file}
    for col in mean_values.index:
        result[f"{col}_avg"] = mean_values[col]
        result[f"{col}_max"] = max_values[col]
        result[f"{col}_min"] = min_values[col]

    return result


def generate_csv_report(folder_path):
    start_time = time.time()

    csv_files = glob.glob(f"{folder_path}/*.csv")

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(process_csv, csv_files)

    report_df = pd.DataFrame(results)
    pd.set_option("display.max_columns", None)
    print("\n=== CSV REPORT ===")
    print(report_df)

    end_time = time.time()
    print(f"\nTime taken (multiprocessing for CSVs): {end_time - start_time:.2f} seconds")


# -------------------------------
# Factorial Functions
# -------------------------------
def factoriel(n):
    return math.factorial(n)


def parallel_factorials(nombres):
    print("\n=== VERSION PARALLÈLE (Factorials) ===")
    debut_para = time.time()

    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        resultats_para = pool.map(factoriel, nombres)

    temps_para = time.time() - debut_para
    print(f"Numbers: {nombres}")
    print(f"Factorials: {resultats_para}")
    print(f"Time taken (parallel factorials): {temps_para:.2f} seconds")


if __name__ == "__main__":
    # Generate CSV report
    generate_csv_report("data")

    # Example factorial numbers
    nombres = [10, 20, 30, 40, 50]
    parallel_factorials(nombres)