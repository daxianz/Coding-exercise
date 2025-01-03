;大小写转换问题

assume cs:codesg,ds:datasg

datasg segment
    db 'BaSiC' ;全转大写 ,dw定义字型数据。word
    db 'iNfOrMaTiOn' ;db定义字节型数据，byte
datasg ends

codesg segment
start: 
    mov ax,datasg
    mov ds,ax
    
    mov cx,5
    mov bx,0
s:  mov al,ds:[bx]
    and al,1011111b
    mov ds:[bx],al
    inc bx
    loop s

    mov cx,11
    mov bx,5
s0:  mov al,ds:[bx]
    or al,0100000b
    mov ds:[bx],al
    inc bx
    loop s0
    
    mov ax,4c00h
    int 21h
codesg ends

end start