import json, csv

class Data:

    def __init__(self, path, type):
        self.path = path
        self.type = type
        self.data = self.r_data()
        self.columns = self.get_columns()
        self.lines = self.size_data()


    def r_json(self):
        json_data = []
        with open(self.path, 'r') as file:
            json_data = json.load(file)
            return json_data


    def r_csv(self):
        csv_data = []

        with open(self.path, 'r') as file:
            # csv reading tool
            spamreader = csv.DictReader(file, delimiter=',')

            for row in spamreader:
                csv_data.append(row)

        return csv_data


    def r_data(self):
        data = []

        if self.type == 'json':
            data = self.r_json()
        
        if self.type == 'csv':
            data = self.r_csv()

        if self.type == 'list':
            data = self.path
            self.path = 'memory list'

        return data


    def get_columns(self):
        return list(self.data[-1].keys())


    def rename_columns(self, key_mapping):
        new_data_csv = []

        for old_dict in self.data:
            dict_temp = {}
            for old_k, value in old_dict.items():
                dict_temp[key_mapping[old_k]] = value
            new_data_csv.append(dict_temp)

        self.data = new_data_csv
        self.columns = self.get_columns()


    def size_data(self):
        return len(self.data)


    def join(dataA, dataB):
        # joining databases
        combined_list = []

        combined_list.extend(dataA)
        combined_list.extend(dataB)

        return Data(combined_list, 'list')


    def table_data(self):
        combined_list_table = [self.columns]

        for row in self.data:
            li = []
            for c in self.columns:
                li.append(row.get(c, 'Unavailable'))
            combined_list_table.append(li)

        return combined_list_table


    def save(self, path):
        combined_data_table = self.table_data()

        with open(path, 'w') as file:
            writer = csv.writer(file)
            writer.writerows(combined_data_table)
