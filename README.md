# FIAP - Faculdade de Informática e Administração Paulista

<p align="center">
<a href= "https://www.fiap.com.br/"><img src="assets/logo-fiap.png" alt="FIAP - Faculdade de Informática e Admnistração Paulista" border="0" width=40% height=40%></a>
</p>

<br>

# Nome do projeto

## Nome do grupo

## 👨‍🎓 Integrantes: 
- <a href="https://www.linkedin.com/in/ian-perez-3b2898341/?skipRedirect=true&contentTrackingId=uAUFJyNmR5y20HPvzqlKHw%3D%3D&viewName=premium-nav-upsell-text&upsellOrderOrigin=Tracking%3Av1%3Apremium_nav_upsell_text%3ANav%3AIn-Product">Ian Lima Perez</a>

## 👩‍🏫 Professores:
### Tutor(a) 
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Tutor</a>
### Coordenador(a)
- <a href="https://www.linkedin.com/company/inova-fusca">Nome do Coordenador</a>


## 📜 Descrição

# Otimização de colheita de Cana-de-Açúcar

## A dificuldade do agronegócio
O Brasil é líder mundial na produção de cana-de-açúcar. Contudo, as perdas durante a colheita, especialmente a mecanizada, chegam a até 15% da produção (contra 5% da manual). Em São Paulo, isso representa uma perda anual de cerca de R$ 20 milhões. A falta de monitoramento em tempo real do volume esperado versus o volume real colhido impede que o produtor ajuste as máquinas ou melhore o planejamento a tempo, resultando em prejuízos irreparáveis safra após safra.

## Solução:
Foi desenvolvido um sistema de linha de comando desenvolvido em Python que atua como um diário de bordo digital para o produtor. Ele permite:
1. O registro de lotes/talhões colhidos (Manuais ou Mecanizados).
2. O cálculo automático da porcentagem de perda.
3. A classificação do status da colheita (Normal, Alerta ou Crítico) para auxiliar na tomada de decisão imediata (ex: parar a colhedora para manutenção).
4. O armazenamento dos dados localmente (JSON e TXT para relatórios rápidos).
5. A integração corporativa via Banco de Dados (Oracle).

## Tecnologias utilizadas
- **Linguagem:** Python 3.x
- **Estruturas de Dados:** Listas, Tuplas, Dicionários (formando uma tabela de memória).
- **Subalgoritmos:** Funções modulares com passagem de parâmetros.
- **Persistência de Dados:** Arquivos `.json`, relatórios em `.txt` e Banco de Dados Oracle (`oracledb`).
- **Validação:** Tratamento rigoroso de exceções (`try-except`) garantindo integridade dos dados.

## 🔧 Como executar o código

Subalgoritmos: função e procedimento com passagem de parâmetros;
Estruturas de dados: lista, tupla, dicionário, tabela de memória;
Manipulação de arquivos: texto e JSON.
Conexão com banco de dados: Oracle.

## 🗃 Histórico de lançamentos
    
* 0.1.0 - 14/10/2026 

## 📋 Licença

<img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/cc.svg?ref=chooser-v1"><img style="height:22px!important;margin-left:3px;vertical-align:text-bottom;" src="https://mirrors.creativecommons.org/presskit/icons/by.svg?ref=chooser-v1"><p xmlns:cc="http://creativecommons.org/ns#" xmlns:dct="http://purl.org/dc/terms/"><a property="dct:title" rel="cc:attributionURL" href="https://github.com/agodoi/template">MODELO GIT FIAP</a> por <a rel="cc:attributionURL dct:creator" property="cc:attributionName" href="https://fiap.com.br">Fiap</a> está licenciado sobre <a href="http://creativecommons.org/licenses/by/4.0/?ref=chooser-v1" target="_blank" rel="license noopener noreferrer" style="display:inline-block;">Attribution 4.0 International</a>.</p>


