from faker import Faker 

fake_database=Faker()
print(fake.name())
print(fake.address())
print(fake.text())
fake_profile=[fake.profile()for i in range(50)]
data=pd.DataFrame(fake_profile)
print(data.head())
