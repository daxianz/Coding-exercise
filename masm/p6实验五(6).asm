;第六章，实验五 (6)
;用push指令将a段中的前8个字型数据逆序保存到b段中

assume cs:codesg,ds:a,ss:b

a segment
    dw 1,2,3,4,5,6,7,8,9,0ah,0bh,0ch,0dh,0eh,0fh,0ffh ; 1以一个字型数据保存
a ends

b segment
    dw 0,0,0,0,0,0,0,0
b ends

codesg segment
start:
    mov ax,a
    mov ds,ax
    
    mov ax,b
    mov ss,ax
    mov sp,0010h

    mov cx,8
    mov bx,0
s:  push [bx]
    add bx,2
    loop s

    mov ax,4c00h
    int 21h
codesg ends

end start