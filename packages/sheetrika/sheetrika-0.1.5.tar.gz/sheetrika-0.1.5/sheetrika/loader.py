from sheetrika.models import SheetrikaConfig
from sheetrika.goo import GooSheetsClient
from sheetrika.ym import YmClient


class SheetrikaLoader:
    """Metrica to G-Sheets loader"""

    config: SheetrikaConfig = None

    def __init__(self, ym_token: str, goo_token: str, config_path: str):
        self.ym = YmClient(ym_token)
        self.goo = GooSheetsClient(goo_token)
        self.config = SheetrikaConfig.from_yaml(config_path)

    def run(self, task_name: str = None, only_print: bool = False):
        tasks = [self.config.get_task(task_name)] if task_name else self.config.tasks

        info = {}
        for task in tasks:
            data = self.ym.get_data(task.query)

            if only_print:
                print(data.table)
                continue

            stat = self.goo.write(task.sheet, data)
            info[task.name] = {
                'headers': data.headers,
                'stat': stat,
            }
        return info
