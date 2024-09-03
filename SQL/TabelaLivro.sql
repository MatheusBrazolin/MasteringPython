drop table if exists sql_livro;
drop table if exists sql_editora;
drop table if exists sql_categorias;
drop table if exists sql_autores;

create table sql_autores (
  id bigserial primary key, 
  nome varchar(255),
  email varchar(255) unique,
  telefone varchar(20),
  bio text
  );

create table sql_categorias (
    id bigserial primary key,
    nome varchar (255) unique
  );

create table sql_editora (
  id bigserial primary key, 
  nome varchar(255),
  telefone varchar(20),
  endereco text
  );

create table sql_livro (
  id bigserial primary key, 
  titulo varchar(250),
  ano int,
  resumo text,
  pagina int,
  isbn varchar(20),

  categoria_id bigint,
  editora_id bigint,
  autor_id bigint,

  constraint fk_id_categoria foreign key (categoria_id) references sql_categorias(id),
  constraint fk_id_editora foreign key (editora_id) references sql_editora(id),
  constraint fk_id_autor foreign key (autor_id) references sql_autores(id)
  );
  
-- alter table livros rename to autores3;

alter table sql_livro
  add preco int;

-- Outra forma de nomer a chave(key):
--   add constraint fk_id_categoria
--   foreign key ( categoria_id)
--   references categoria(id);
  
insert into sql_autores (email, bio, telefone)
  values
  ('Matheusbrazolin@gmail.com', '20 anos aprendendo um pouco mais de SQL', '11989656078'),
  ('fernando@gmail.com', 'Professor de database', '412566995'),
  ('joao@gmail.com', '36 anos', '33652548'),
  ('Marcelohorce@gmail.com', '47 anos de puro gh', '40028974'),
  ('souza@gmail.com', '78 anos ', '11989656078');

update sql_autores
  set nome = 'Matheus Brazolin',
      telefone = '40028922'
where email = 'matheusbrazolin013@gmailcom' ;

delete from sql_autores where id <= 2;

insert into sql_livro (titulo, ano, resumo, pagina, preco)
  values
  ('Piratas do Caribe', '2004', 'Pirata e suas traquinagens', '458', 150),
  ('Casa Monstro', '2015', 'Exploração em uma casa de terror', '452', 75),
  ('Ratão', '2000', 'Rato atras do queijo perdido ', '120', 70),
  ('Messiano Ronaldo', '2018', 'Uma maquina de fazer gol', '801', 500),
  ('Tesouro perdido', '2021', 'Crianças atras do tesouro perdido', '458', 150);

-- select * from sql_livro

-- Alteração de valore:
  update sql_livro
  set preco = 25
  where id = 4 
  returning *; 

