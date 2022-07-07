import json
from SalesReport import SalesReport


class SalesReportJSON(SalesReport):
    def serialize(self):
        with open(self.export_file + '.json', 'w') as file:
            json.dump(self.build(), file)

    def get_length(self):
        return 23


meu_relatorio_de_vendas = SalesReportJSON('json_meu_relatorio')
meu_relatorio_de_vendas.serialize()
print(meu_relatorio_de_vendas.get_length())
