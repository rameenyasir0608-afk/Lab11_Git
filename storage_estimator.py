num_files = int(input("How many files? "))
avg_size_mb = float(input("Average file size in MB? "))
total_mb = num_files * avg_size_mb
print("Total storage needed:", total_mb, "MB")
print("Total storage in GB:", round(total_mb / 1024, 4), "GB")

print("Thank you for using storage estimator!")
