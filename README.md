# XVIII-Chopin-Competition-Statistics-Backend

Try to use AWS API Gateway, Lambda, DynamoDB service build backend.

## Competition Data

The endpoint from https://chopin2020.pl/en/ 

https://cms.chopin2020.pl/participants/{numbers}

## Repertoires Data

https://imslp.org/wiki/Category:Chopin,_Fr%C3%A9d%C3%A9ric

## DynamoDB

### table

* Stages

    {
        'id': number,
        'name': string,
        'create_at': ,
        'update_at':
    }

* Repertoires

    {
        'id': number,
        'serial': string, #opus or B
        'opus': number,
        'number': number,
        'genre': string,
        'name': string,
        'tonality': string,
        'remark': string,
        'create_at': ,
        'update_at':
    }

* Repertoires Pool

    {
        'id': number,
        'stages': {},
        'repertoires': [],
        'choose': number,
        'create_at': ,
        'update_at':
    }

* Competitors

    {
        'id': ,
        'full_name': ,
        'birth_date': ,
        'create_at': ,
        'update_at': 
    }

* Nations

    {
        'id': ,
        'name': ,
        'create_at': ,
        'update_at': 
    }