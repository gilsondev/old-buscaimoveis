# Busca Imóveis

Sistema voltado para agregação de anúncios de imóveis. Alguns dos serviços coletados no momento são:

 - OLX

Em breve para os seguintes serviços:

 - ZAP Imóveis
 - Viva Real

Todos os anúncios são coletados via crawling usando o [Busca Imóveis Scraper](https://github.com/gilsondev/buscaimoveis-scraper).


## Instalação

Faça o checkout do projeto:

```shell
$ git clone https://github.com/gilsondev/buscaimoveis
```

Prepare o ambiente com virtualenv e instale as dependências:

```shell
$ python3 -m venv .venv
$ source .venv/bin/activate
$ make install
```

Então inicie o servidor local:

```shell
$ bimoveis runserver
```

## Testes

O projeto usa Selenium para testes de aceitação. Com isso é recomendável ter o PhantomJS instalado. Com tudo pronto digite o comando:

```shell
$ make test
```

## Outros comandos

Mais dúvidas sobre os comandos disponíveis, digite os comandos abaixo:


```shell
$ make help

Usage:
  make <target>

Targets:
  help        Display this help
  clean       remove Python file artifacts
  test        run tests quickly with the default Python
  install     install the package to the active Python's site-packages
```

```shell
$ bimoveis

Usage: bimoveis [OPTIONS] COMMAND [ARGS]...

  Busca Imóveis APP

Options:
  --help  Show this message and exit.

Commands:
  runserver  Run the server with dev/debug mode
  shell      Open a shell with app in the context
```

## Como Contribuir
Veja mais no arquivo `CONTRIBUTING.md`, as formas de ajudar com o projeto, e o `AUTHORS.md` para saber quem estão a frente e que pode te auxiliar.
