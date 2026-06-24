import math
#Day 5
#Exercises: Level 1
#1-9
empty_list = []
five_list = ["one", "two", "three", "four", "jhin"]
print(len(five_list))
print(five_list[0], five_list[2], five_list[-1])
mixed_data_types = ["Eric", 200, 193, True, "location address"]
it_companies = ["Facebook", "Google", "Microsoft", "Apple", "IBM", "Oracle", "Amazon"]
print(it_companies)
print(len(it_companies))
print(it_companies[0], it_companies[3], it_companies[-1])

#10
it_companies[0] = "Ten"
print(it_companies)

#11
it_companies.append("Eleven")
print(it_companies)

#12
it_companies.insert(5, "Twelve") #Theres 8 companies now? middle is 4 or 5
print(it_companies)

#13
upper = str(it_companies[0])
print(upper.upper())

#14-15
print("#; ".join(it_companies))
print("IBM" in it_companies)

#16
sorted_companies = it_companies.sort()
print(it_companies)

#17
reverse_sort = it_companies.sort(reverse=True)
print(it_companies)

#18-20
print(len(it_companies))
print(it_companies[0:3])
print(it_companies[6:9])
print(it_companies[3:6])

#21
it_companies.pop(0)
print(it_companies)

#22
it_companies.pop(3)
it_companies.pop(3)
print(it_companies)

#23
it_companies.pop()
print(it_companies)

#24
it_companies.clear()
print(it_companies)

#25
del it_companies
#print(it_companies)      check if it_companies still there

#26
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node','Express', 'MongoDB']
new_end = front_end + back_end
print(new_end)

#27
full_stack = new_end.copy()
full_stack.insert(5, "Python")
full_stack.insert(6, "SQL")
print(full_stack)

#Exercises: Level 2
ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]

ages_ordered = ages.sort()
print(ages) #min age = 19, max age = 26

ages.insert(0, 19)
ages.insert(-1, 26)
print(ages)

n = len(ages)
median = ages[n//2]
print(median)

average = sum(ages)/n
print(average)

max = ages[-1]
min = ages[0]
range = max-min
print(range)

lower_dev = abs(min-average)
upper_dev = abs(max-average)
print(f"Lower deviation: {lower_dev}. Upper deviation: {upper_dev}")

countries = countries = [
  'Afghanistan',
  'Albania',
  'Algeria',
  'Andorra',
  'Angola',
  'Antigua and Barbuda',
  'Argentina',
  'Armenia',
  'Australia',
  'Austria',
  'Azerbaijan',
  'Bahamas',
  'Bahrain',
  'Bangladesh',
  'Barbados',
  'Belarus',
  'Belgium',
  'Belize',
  'Benin',
  'Bhutan',
  'Bolivia',
  'Bosnia and Herzegovina',
  'Botswana',
  'Brazil',
  'Brunei',
  'Bulgaria',
  'Burkina Faso',
  'Burundi',
  'Cabo Verde',
  'Cambodia',
  'Cameroon',
  'Canada',
  'Central African Republic',
  'Chad',
  'Chile',
  'China',
  'Colombia',
  'Comoros',
  'Congo, Democratic Republic of the',
  'Congo, Republic of the',
  'Costa Rica',
  "Côte d'Ivoire",
  'Croatia',
  'Cuba',
  'Cyprus',
  'Czech Republic',
  'Denmark',
  'Djibouti',
  'Dominica',
  'Dominican Republic',
  'East Timor (Timor-Leste)',
  'Ecuador',
  'Egypt',
  'El Salvador',
  'Equatorial Guinea',
  'Eritrea',
  'Estonia',
  'Eswatini',
  'Ethiopia',
  'Fiji',
  'Finland',
  'France',
  'Gabon',
  'Gambia',
  'Georgia',
  'Germany',
  'Ghana',
  'Greece',
  'Grenada',
  'Guatemala',
  'Guinea',
  'Guinea-Bissau',
  'Guyana',
  'Haiti',
  'Honduras',
  'Hungary',
  'Iceland',
  'India',
  'Indonesia',
  'Iran',
  'Iraq',
  'Ireland',
  'Israel',
  'Italy',
  'Jamaica',
  'Japan',
  'Jordan',
  'Kazakhstan',
  'Kenya',
  'Kiribati',
  'Korea, North',
  'Korea, South',
  'Kuwait',
  'Kyrgyzstan',
  'Laos',
  'Latvia',
  'Lebanon',
  'Lesotho',
  'Liberia',
  'Libya',
  'Liechtenstein',
  'Lithuania',
  'Luxembourg',
  'Madagascar',
  'Malawi',
  'Malaysia',
  'Maldives',
  'Mali',
  'Malta',
  'Marshall Islands',
  'Mauritania',
  'Mauritius',
  'Mexico',
  'Micronesia',
  'Moldova',
  'Monaco',
  'Mongolia',
  'Montenegro',
  'Morocco',
  'Mozambique',
  'Myanmar',
  'Namibia',
  'Nauru',
  'Nepal',
  'Netherlands',
  'New Zealand',
  'Nicaragua',
  'Niger',
  'Nigeria',
  'North Macedonia',
  'Norway',
  'Oman',
  'Pakistan',
  'Palau',
  'Palestine',
  'Panama',
  'Papua New Guinea',
  'Paraguay',
  'Peru',
  'Philippines',
  'Poland',
  'Portugal',
  'Qatar',
  'Romania',
  'Russia',
  'Rwanda',
  'Saint Kitts and Nevis',
  'Saint Lucia',
  'Saint Vincent and the Grenadines',
  'Samoa',
  'San Marino',
  'Sao Tome and Principe',
  'Saudi Arabia',
  'Senegal',
  'Serbia',
  'Seychelles',
  'Sierra Leone',
  'Singapore',
  'Slovakia',
  'Slovenia',
  'Solomon Islands',
  'Somalia',
  'South Africa',
  'South Sudan',
  'Spain',
  'Sri Lanka',
  'Sudan',
  'Suriname',
  'Sweden',
  'Switzerland',
  'Syria',
  'Tajikistan',
  'Tanzania',
  'Thailand',
  'Togo',
  'Tonga',
  'Trinidad and Tobago',
  'Tunisia',
  'Turkey',
  'Turkmenistan',
  'Tuvalu',
  'Uganda',
  'Ukraine',
  'United Arab Emirates',
  'United Kingdom',
  'United States',
  'Uruguay',
  'Uzbekistan',
  'Vanuatu',
  'Vatican City',
  'Venezuela',
  'Vietnam',
  'Yemen',
  'Zambia',
  'Zimbabwe'
]

mid = (len(countries) + 1) // 2
upper_half = countries[:mid]
lower_half = countries[mid:]
print(upper_half)
print(lower_half)

other_countries = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(other_countries[0] + "\n" + other_countries[1] + "\n" + other_countries[2])
scandic = other_countries[3:]
print(f"Scandic countries: {scandic}")