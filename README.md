# scan-ports

Este script em Python é um scanner de portas simples que utiliza o protocolo TCP para verificar se determinadas portas estão abertas em um alvo especificado (pode ser um IP ou domínio). Ele também tenta identificar o serviço associado a cada porta aberta usando um mapeamento de portas conhecidas.

## Funcionalidade

O script realiza as seguintes ações:
1. Solicita ao usuário o **IP ou domínio** do alvo.
2. Solicita ao usuário o intervalo de **portas** (de porta inicial a porta final) para escanear.
3. Para cada porta no intervalo fornecido, cria uma **thread** para verificar se a porta está aberta.
4. Ao identificar uma porta aberta, o script exibe o número da porta e o serviço correspondente (se mapeado).
5. O tempo de **timeout** para cada tentativa de conexão é definido como 0.5 segundos, o que permite uma execução mais rápida.

## Portas Conhecidas e seus Serviços

O script faz um mapeamento simples das seguintes portas para seus respectivos serviços:

- **21**: FTP
- **22**: SSH
- **23**: Telnet
- **25**: SMTP
- **53**: DNS
- **80**: HTTP
- **110**: POP3
- **143**: IMAP
- **443**: HTTPS
- **3306**: MySQL
- **3389**: RDP

Se a porta não estiver mapeada, o serviço será exibido como "Desconhecido".

## Requisitos

- Python 3.x
- Biblioteca `socket` (já inclusa na instalação padrão do Python)
- Biblioteca `threading` (também padrão no Python)
