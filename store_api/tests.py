from rest_framework.test import APITestCase
from rest_framework import status
from .models import store
from rest_framework.reverse import reverse as api_reverse

# Create your tests here.

class StoreAPITestCase(APITestCase):
    def setUp(self):
        store_item= store.objects.create(
            key= 'baha',
            value='123423'
        )

    def test_single_store(self):
        item_count= store.objects.count()
        self.assertEqual(item_count,1)

    def test_get_list(self):
        data={}
        url=api_reverse("api-store:store-create")
        response=self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_post_item(self):
        data=    {
                "pk": 42,
                "key": "jawad",
                "value": "luchu"
                }
        url = api_reverse("api-store:store-create")
        response=self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_get_item(self):
        value= store.objects.first()
        data={}
        url= '/api/store/{}/'.format(value.pk)
        response= self.client.get(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_item(self):
        value= store.objects.first()
        url = '/api/store/{}/'.format(value.pk)
        data={
            "pk": 36,
            "key": "baha",
            "value": "123217"
        }
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)