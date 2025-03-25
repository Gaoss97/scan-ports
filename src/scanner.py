import socket
import threading

# Mapeamento de portas conhecidas para serviços
services = {
    21: "FTP",
    22: "SSH",
    23: "Telnet",
    25: "SMTP",
    53: "DNS",
    80: "HTTP",
    110: "POP3",
    143: "IMAP",
    443: "HTTPS",
    3306: "MySQL",
    3389: "RDP"
}

def scan_port(target, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(0.5)

    if sock.connect_ex((target, port)) == 0:
        service = services.get(port, "Desconhecido")
        print(f"1 Porta {port} aberta ({service})")
    sock.close()

def scan_ports(target, start_port, end_port):
    print(f"Escaneando {target} nas portas {start_port} - {end_port}")

    threads = []
    for port in range(start_port, end_port + 1):
        thread = threading.Thread(target=scan_port, args=(target, port))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

if __name__ == "__main__":
    alvo = input("Digite o IP ou domínio do alvo: ")
    porta_inicial = int(input("Porta inicial: "))
    porta_final = int(input("Porta final: "))

    scan_ports(alvo, porta_inicial, porta_final)
