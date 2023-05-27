from random import random

from factory import Factory
import pandas as pd
import factory


class WorkerFactory(Factory):
    class Meta:
        model = dict

    name = factory.Faker('first_name')
    age = factory.Faker('random_int', min=18, max=60)
    position = factory.Faker('job')
    salary = factory.Faker('random_int', min=5000, max=8000)
    length_of_service = factory.Faker('random_int', min=1, max=30)


num_rows = 40

workers = WorkerFactory.create_batch(num_rows)

for worker in workers:
    if random() < 0.1:
        worker['salary'] = int("-" + str(worker['salary']))
    if random() < 0.1:
        worker['position'] = None


df = pd.DataFrame(workers)
df.to_csv("workers_csv.csv")

print(df)
