import matplotlib
matplotlib.use('Agg')  # Evita abrir janelas GUI
import matplotlib.pyplot as plt
import io
import base64

class RelatorioService:
    def __init__(self, resposta_repository):
        self.resposta_repository = resposta_repository

    def gerar_graficos_por_questao(self, filmeid):
        questoes = self.resposta_repository.get_respostas_por_questao(filmeid)
        graficos = []

        opcoes_possiveis = ["Sim", "Não", "Talvez"]

        for qid, dados in questoes.items():
            plt.figure(figsize=(8, 4))
            respostas = dados['respostas']

            # Garantir que todas as opções apareçam
            contagem = [respostas.get(op, 0) for op in opcoes_possiveis]
            total = sum(contagem) if sum(contagem) > 0 else 1  # evita divisão por zero
            porcentagens = [c / total * 100 for c in contagem]

            bars = plt.bar(opcoes_possiveis, contagem, color='skyblue')
            plt.title(dados['texto'])
            plt.xlabel("Resposta")
            plt.ylabel("Quantidade")

            # Adicionar valor e porcentagem no topo da barra
            for bar, c, p in zip(bars, contagem, porcentagens):
                plt.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.1,
                         f"{c} ({p:.0f}%)",
                         ha='center', va='bottom', fontsize=10)

            plt.tight_layout()

            # Converter gráfico para base64
            buf = io.BytesIO()
            plt.savefig(buf, format='png')
            buf.seek(0)
            img_base64 = base64.b64encode(buf.read()).decode('utf-8')
            buf.close()
            plt.close()

            graficos.append(img_base64)

        return graficos

