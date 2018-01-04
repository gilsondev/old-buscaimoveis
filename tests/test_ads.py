def test_should_return_status_200(app):
    with app.test_client() as client:
        response = client.get('/')
        assert response.status_code == 200


def test_should_contain_ads_list_content(app):
    with app.test_client() as client:
        response = client.get('/')

        contents = [
            '<h1 class="text-center">Busca Imóveis</h1>',
            '<form action=".">'
        ]

        for content in contents:
            assert content in str(response.data)
