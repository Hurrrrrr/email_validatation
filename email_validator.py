import csv

output_list = []
first_name = input("Enter first name: ")
last_name = input("Enter last name: ")
domain = input("Enter domain (no @ symbol): ")

output_list.append(f"{first_name}@{domain}")
output_list.append(f"{last_name}@{domain}")
output_list.append(f"{first_name}{last_name}@{domain}")
output_list.append(f"{first_name}.{last_name}@{domain}")
output_list.append(f"{first_name[0]}{last_name[0]}@{domain}")
output_list.append(f"{first_name[0]}{last_name}@{domain}")
output_list.append(f"{first_name[0]}.{last_name}@{domain}")
output_list.append(f"{first_name}{last_name[0]}@{domain}")
output_list.append(f"{first_name}.{last_name[0]}@{domain}")

print(output_list)

with open("./emails.txt", "w") as f:
    writer = csv.writer(f)
    for email in output_list:
            writer.writerow([email])