from locust import HttpLocust, TaskSet, task
import json

ENDPOINT = "/_sql"
OneK = "DLZFR8HDRMEY89ECUGXG317GGJO6TXGR709WC01NN9XALB4WS8117VX99D79Q8YIZC7IMSNHVVCCR8F7JUEAYRG11EK7HD4NVCPNTC4X6AROOZKWT8CD3A9YPMRBN8K6PHU8XCO877CI5ANYPB899N9HNS3MOTDBAUE0E7WIAXQZ9IQTGDXL209AWQX9UAMO9ZNLD0OW7AFVODLJPT44GMDFNX2LTUZ07VMIOSPVGN794JWONAJL3W9TK95ONHF0VAPZLFP68H4ODV4W63CQ32H8M31T96BI0FS0KZHUFLFV8VOWS1YCSLOP9V1G6W2086XTN2YKWCCCQYZ932USSLE691L36MOOZVFEZL7HN3QNR74EKOTW6ZWA9NVF7Z0X5XPP2HNKKKWZ54VNB6GJO6999GMZ4NPGB8IESIZAESHBJL4U1Q5D741AG19N93R37071U4YI0FJNK9XND3M8PPK1BALF68EFFOG8UGGD2I5T9W6DJM6KBVDHY2NV0TRTWU4ZC8O4JIJHQTKAV8OCPWUTDKQV494B1GYBZA29CMW60NIG2ZS5KFBTGY2ALK1TQE7TD6N8KR9EIM4785FTFKPAL20JCE8WPU30GSQZFQTLD3U1M0WY1PMEOYNSLF5FNEQPVNUKIUV3XG3GQY96Q7LNGGMW1BMVRVE94KL4SR45X4FHCK6FLG4R952VJGZNP2KV8GKZ076ZNMILPEXHZXURZLPP0H44M53TJSFG0KUE4IKYP5PLZ78YT48MX8VY6GC9WIM0BHJ5QFLJQC7R8SSYDJ0IVU0JXNL4X7LPLGY5X45FSS4YGOY0JU48S8UIZGUMPNMXFVAJUH4556763LPMMOKQJKTPBZO9QRH94EOG3BBZOTJ6XKRXDIYNXENW254T4S7YGW1UW2FB1I9PEKUB3BJJ6S94NZ8HJGE6KTL0ARPMD5CVOJ68GO34LA5ZBLIHPVQU1XWMXD1EV1FZSLSXJDYZV9V70VHERVJD59Z9S1BU69PW8PY76CVHLHC4"


class InsertUpdateAndRead(TaskSet):

    def on_start(self):
        bulk_size = 10000
        num_records = bulk_size

        self.num_reads = 10000
        self.num_inserts = 1  # * bulk_size * OneK

        table = "loadtest"

        self.insert = "insert into {table} (data) values (?)".format(
            table=table)
        self.select = "select * from {table} limit 10000".format(table=table)

        self.bulk_args = [(OneK, )] * bulk_size

        self.payload_insert = json.dumps(
            {"stmt": self.insert, "bulk_args": self.bulk_args})
        self.payload_insert_single = json.dumps({"stmt": "insert into {table} (data) values ('{onek}')".format(table=table, onek=OneK)})
        self.payload_read = json.dumps({"stmt": self.select})
        print self.payload_insert_single

    @task(8)
    def insert10ksingle(self):
        for ins in range(self.num_inserts):
            self.client.request('post',
                ENDPOINT, data = self.payload_insert_single, headers = {"ContentType": "application/json"})
    # @task(8)
    # def insert10k(self):
    #     for ins in range(self.num_inserts):
    #         self.client.request('post',
    #             ENDPOINT, data = self.payload_insert, headers = {"ContentType": "application/json"})


    @task(2)
    def read10k(self):
        for ins in range(self.num_reads):
            self.client.request('post',
                ENDPOINT, data = self.payload_read, headers = {"ContentType": "application/json"})


class LoadTester(HttpLocust):
    task_set = InsertUpdateAndRead
    min_wait = 0
    max_wait = 0
