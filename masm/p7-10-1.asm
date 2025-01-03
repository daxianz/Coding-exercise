;将Datasg段中的每个单词的首字母大写

assume cs:codesg,ds:datasg

datasg segment
    db '1.file          '
    db '2.edit          '
    db '3.search        '
    db '4.view          '
    db '5.options       '
    db '6.help          '
datasg ends

codesg segment
start: 
    mov ax,datasg
    mov ds,ax

    mov cx,6
    mov bx,2
s:  mov al,[bx]
    and al,11011111b
    mov [bx],al
    add bx,16
    loop s

    mov ax,4c00h
    int 21h
codesg ends

end start
