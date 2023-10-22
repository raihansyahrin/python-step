import requests

# Menambahkan data dengan metode POST
data_post = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 1849.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB"
    }
}
url_post = 'https://api.restful-api.dev/objects'
response_post = requests.post(url_post, json=data_post)
print(f'POST: {response_post.status_code}, {response_post.json()}')

# Memperbarui data dengan metode PUT
new_id_put = response_post.json()['id']
data_put = {
    "name": "Apple MacBook Pro 16",
    "data": {
        "year": 2019,
        "price": 2049.99,
        "CPU model": "Intel Core i9",
        "Hard disk size": "1 TB",
        "color": "silver"
    }
}
url_put = url_post + '/' + str(new_id_put)
response_put = requests.put(url_put, json=data_put)
print(f'\nPUT: {response_put.status_code}, {response_put.json()}')

# Mendapatkan data dengan metode GET
url_get = 'https://api.restful-api.dev/objects/7'
response_get = requests.get(url_get)
print(f'\nGET: {response_get.status_code}, {response_get.json()}')

# Menghapus data dengan metode DELETE
new_id_delete = response_post.json()['id']
url_delete = url_post + '/' + str(new_id_delete)
response_delete = requests.delete(url_delete)
print(f'DELETE: {response_delete.status_code}, {response_delete.json()}')