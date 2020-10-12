from django.apps import AppConfig
from django.forms import model_to_dict
from .models import Block, average
import json
from Crypto.Hash import SHA256
import pandas as pd
from datetime import datetime
from pprint import pprint
from collections import OrderedDict


class BlockConfig(AppConfig):
    name = 'block'


class Chain:
    model = Block

    def __init__(self, modelName=Block, uid=0):
        self.UserId = uid
        self.blocks = [{'verified': False, 'data': x} for x in self.model.objects.filter(
            UserId=uid).order_by('-created_on')]
        self.verify()

    @classmethod
    def compile_id(cls, uid):
        print("Anon for uid", uid)
        return pd.DataFrame(list(Block.objects.filter(UserId=uid).order_by('-created_on').values()[:1]))

    @classmethod
    def compile_all(cls):
        objects = list(cls.model.objects.all().order_by(
            'UserId', '-created_on').distinct().values())
        df = pd.DataFrame(objects)
        return df

    @classmethod
    def create_hash(cls, data):
        # data = OrderedDict(sorted())
        for x in ['my_hash']:
            try:
                del data[x]
            except Exception as e:
                pass

        mess = json.dumps(data)
        h = SHA256.new()
        h.update(mess.encode('utf-8'))
        return h.digest().decode('utf-8', errors='replace')

    def get_previous_hash(self):
        if len(self.blocks) == 0:
            return ''
        else:
            return self.blocks[0]['data'].my_hash

    def verify(self):
        '''
        This Function will create / match hash
        '''
        verified = True
        blocks = list(reversed(self.blocks))
        for i in range(len(self.blocks)):

            if blocks[i]['data'].previous_hash in ['', None] and i != 0:
                blocks[i]['data'].previous_hash = blocks[i -
                                                         1]['data'].my_hash
                blocks[i]['data'].save()
            if blocks[i]['data'].my_hash in ['', None]:
                if i != 0:
                    blocks[i]['data'].previous_hash = blocks[i -
                                                             1]['data'].my_hash
                data = model_to_dict(blocks[i]['data'])
                blocks[i]['data'].my_hash = Chain.create_hash(data)
                blocks[i]['data'].save()

            if i == 0:
                # print("I was here 0")
                blocks[i]['verified'] = True
            elif blocks[i-1]['verified'] == False:
                print("I was here 1")
                blocks[i]['verified'] = False
                verified = False
            else:
                print("I was here 2")
                data = model_to_dict(blocks[i - 1]['data'])
                if blocks[i]['data'].previous_hash == Chain.create_hash(data) == blocks[i-1]['data'].my_hash:
                    blocks[i]['verified'] = True
                else:
                    print(blocks[i]['data'].previous_hash, '  --:--\t--:--  ',
                          Chain.create_hash(data))
                    blocks[i]['verified'] = False
                    verified = False

        return verified

    def compiled_result(self):
        cols = list(
            filter(
                lambda x:
                x not in ['previous_hash',
                          'my_hash', 'created_on'],
                map(
                    lambda x:
                    x.name,
                    Block._meta.get_fields()
                )
            )
        )
        d = pd.DataFrame(
            columns=cols,
            rows=[[
                self.blocks[0][name] for name in cols
            ]]
        )

    def to_list(self):
        res = []
        for block in self.blocks:
            try:
                created_on = str(block['data'].created_on)
            except Exception as identifier:
                print(block, self.blocks)
                return res
            b = {}
            b.update(block)
            b['data'] = model_to_dict(block['data'])
            b['data']['created_on'] = str(created_on)
            del b['data']['my_hash']
            del b['data']['previous_hash']
            res.append(b)

        # pprint(res)
        return res

    def add_updates(self, **kwargs):
        kwargs.update({
            'UserId': self.UserId,
            'previous_hash': self.get_previous_hash(),
        })
        for x in ['my_hash', 'id']:
            try:
                del kwargs[x]
            except Exception as e:
                pass

        '''mHash = Chain.create_hash(kwargs)
        kwargs.update({
            'my_hash': mHash
        })'''
        block = Block(**kwargs)
        block.save()
        self.blocks.insert(0, {'verified': True, 'data': block})
        self.verify()


def get_connection():
    from django.conf import settings
    from sqlalchemy import create_engine

    user = settings.DATABASES['default']['USER']
    password = settings.DATABASES['default']['PASSWORD']
    database_name = settings.DATABASES['default']['NAME']

    string = "{dialect}://{username}:{password}@{host}/{database}".format(
        dialect='mysql',
        username=user,
        password=password,
        host='localhost',
        database=database_name
    )

    return create_engine(string, echo=False)


def fill_sample(file_name='block/anonymous/finalized.csv'):
    # Checking if objects exists or not
    if len(Block.objects.all()) != 0:
        raise "Data Not Empty"

    df = pd.read_csv(file_name).rename(columns={
        'ID': 'UserId'
    })

    df['previous_hash'] = ''
    df['my_hash'] = ''
    df['created_on'] = datetime.now()

    # Adding mean values
    fields = []
    for field in Block._meta.get_fields():
        fields.append(field.name)
        if field.name in ['UserId']:
            continue
        if field.name in average:
            if field.name not in df:
                df[field.name] = average[field.name]
            else:
                df[field.name] = df[field.name].fillna(average[field.name])
        else:
            print("Warning : field", field.name,
                  " not present in avg do you want to continue anyway?(y/n0):")
            res = input()
            if res == 'n':
                return

    print(fields)
    fields = [f for f in fields if f in df.columns]

    df = df.loc[:, fields]

    df.to_sql('block_block', con=get_connection(),
              if_exists='append',
              index=False
              )
