import requests


def get_address_from_docker_service(cep):
    docker_service_url = 'http://localhost:5000/cep/'
    response = requests.get(docker_service_url + cep)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return None


def pesquisa_cep():
    erro_entrada = True
    continua_pesquisa = True

    while erro_entrada and continua_pesquisa:
        cep = input("\nDigite o CEP para consultar: ")
        address_data = get_address_from_docker_service(cep)
        if address_data:
            print("\n")
            titulo = "- D A D O S  D O  E N D E R E Ç O -"
            print("=" * len(titulo))
            print(titulo)
            print("=" * len(titulo))
            print(" CEP       : ", address_data['cep'])
            print(" Logradouro: ", address_data['logradouro'])
            print(" Bairro    : ", address_data['bairro'])
            print(" Cidade    : ", address_data['localidade'])
            print(" Estado    : ", address_data['uf'])

            # erro_entrada = False  # Encerra o loop
        else:
            print("CEP não encontrado ou serviço indisponível.")

        aux = input('Continuar pesquisando? [s/n]: ').upper().strip()
        if aux != 'N':
            # Encerra o loop
            continua_pesquisa = False
            erro_entrada = False


if __name__ == '__main__':
    pesquisa_cep()
