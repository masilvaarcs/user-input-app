# user_input_app

## Descrição

O user_input_app é uma aplicação simples em Python que permite aos usuários inserir um CEP e consultar os dados de endereço correspondentes usando o serviço Docker_Service que roda no Docker.

## Requisitos

Antes de executar o user_input_app, certifique-se de ter o seguinte instalado em sua máquina:

- Python 3.x
- Biblioteca "requests" (instalada com pip, utilizada para fazer requisições HTTP)

## Como usar

1. Clone este repositório para sua máquina local.

2. Navegue até a pasta do projeto user_input_app.

3. Execute o seguinte comando para iniciar o aplicativo:

```bash
python app.py
```

4. O aplicativo solicitará que você digite um CEP.

5. Após inserir o CEP, o aplicativo fará uma requisição ao serviço user_input_app que roda no Docker para consultar os dados do endereço associado ao CEP informado.

6. O aplicativo exibirá os dados do endereço na tela, se o CEP for encontrado.

7. Será lhe perguntado: *Continuar pesquisando? [s/n]: onde deverá ser informado S para Sim ou N para Não. Qualquer entrada diferente de N (Não) encerrará o programa.* 


## Contribuição

Se você encontrar algum problema ou tiver alguma sugestão de melhoria, sinta-se à vontade para abrir uma "Issue" neste repositório. Contribuições através de "Pull Requests" também são bem-vindas!

## Licença

Este projeto está licenciado sob a Licença MIT - consulte o arquivo [LICENSE](LICENSE) para obter detalhes.
```

Agora você pode copiar e colar os modelos acima nos arquivos `README.md` de cada projeto e personalizá-los com informações específicas do seu projeto. Isso deve ajudá-lo a criar um README.md bem estruturado e profissional para ambos os projetos no GitHub.