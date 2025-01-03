;编程，将每个datasg段中每个单词改为大写字母

assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    db 'ibm             '
    db 'dec             '
    db 'dos             '
    db 'vax             '
datasg ends

stacksg segment
    dw 0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
stacksg ends

codesg segment
start:
    mov ax,datasg
    mov ds,ax
    mov ax,stacksg
    mov ss,ax
    mov sp,32

    mov cx,4
    mov di,0
s0: push cx
    mov bx,0
    mov cx,3
s:  mov al,[bx+di]
    and al,11011111b
    mov [bx+di],al
    inc bx
    loop s

    add di,16
    pop cx
    loop s0

    mov ax,4c00h
    int 21h
codesg ends
end start
