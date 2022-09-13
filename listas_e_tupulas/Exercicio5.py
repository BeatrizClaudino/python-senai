#frase = {'E''s''s''e' 'é' 'u''m' 't''e''s''t''e' 'p''a''r''a' 'm''e''d''i'r'' 'm''e''u''s''c''o''n''h''e''c''i''m''e''n''t''o''s'' e''m'' ''p''y''t''h''o''n'}
conte=0
cont=0
frase = "Esse é um teste para medir meus conhecimentos em python"

for i in frase:
    if 'e' == i:
        conte += 1
        print("tem")
    if 's' == i:
        cont +=1

print(cont)