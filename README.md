# Raspagem IoT

Exemplos simples de aplicações de raspagem de dados utilizando a placa Intel Edison.

<img src="edison.jpg" style="height: 200px;"/>

## Pré-requisitos
- [Python 2.7](https://www.python.org/downloads/release/python-2713/)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/#installing-beautiful-soup)
- [requests](https://github.com/requests/requests)
- [upm](https://github.com/intel-iot-devkit/upm/blob/master/docs/installing.md)
- [Kit Intel Edison para Arduino](https://www.intel.com.br/content/www/br/pt/products/boards-kits/edison/kit-for-arduino.html)
- [Grove - Starter Kit Plus Gen 2](https://www.seeedstudio.com/Grove-starter-kit-plus-Intel-IoT-Edition-for-Intel-Galileo-Gen-2-and-Edison-p-1978.html)

## Instalação

Acesse o Edison

```
# Substitua 'edison-lmayra' pelo nome da sua placa
$ ssh root@edison-lmayra.local
```
Informações referentes à configuração inicial da placa podem ser encontradas na [Wiki](https://github.com/lidimayra/raspagem-iot/wiki/Setup).

Faça o clone do projeto e acesse a pasta recém-criada

```
# git clone git@github.com:lidimayra/raspagem-iot.git && cd raspagem-iot
```

O único script existente até o momento é um rastreador do sistema dos correios que exibe o status da encomenda no LCD.

Execute o script passando como parâmetro o número do pedido de rastreamento:

```
# python script.py SS123456789BR
```

