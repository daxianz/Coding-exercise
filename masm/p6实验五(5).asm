;第六章，实验五
;(5)将a段，b段的数据依次相加，结果保存在c段中

assume cs:code,ds:c

a segment
    db 1,2,3,4,5,6,7,8
a ends

b segment
    db 1,2,3,4,5,6,7,8
b ends

c segment
    db 0,0,0,0,0,0,0,0
c ends

code segment
start:
    mov ax,c
    mov ds,ax

    mov ax,a
    mov es,ax

    mov cx,8
    mov bx,0
s:  mov ax,es:[bx]
    add ds:[bx],ax
    inc bx
    inc bx
    loop s

    mov ax,b
    mov es,ax

    mov cx,8
    mov bx,0
s0: mov ax,es:[bx] 
    add ds:[bx],ax
    inc bx
    inc bx
    loop s0

    mov ax,4c00h
    int 21h
code ends

end start