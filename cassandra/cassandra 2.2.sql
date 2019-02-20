
CREATE KEYSPACE pucdemo
WITH REPLICATION = { 'class' : 'SimpleStrategy', 'replication_factor':1};


CREATE TABLE aluno
AND key_validation_class=UTF8Type
AND column_metadata = [
{column_name: nome, validation_class: UTF8Type}
{column_name: email, validation_class: UTF8Type}
{column_name: estado_civil, validation_class: UTF8Type}
{column_name: sexo, validation_class: UTF8Type}
{column_name: idade, validation_class: LongType}];

CREATE TABLE pucdemo.aluno ( id UUID PRIMARY KEY, nome text, email text, estado_civil text, sexo text, idade int );

insert into pucdemo.aluno (id, nome, email, estado_civil, sexo, idade) values(now(), 'nome do aluno1',
'meu_email@noemail.com','solteiro','M',25);


insert into pucdemo.aluno (id, nome, email, estado_civil, sexo, idade) values(now(), 'nome do aluno2',
'meu_email@noemail2.com','casado','F',37);
