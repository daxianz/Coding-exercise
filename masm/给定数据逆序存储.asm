assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    dw 0123h,0456h,0789h,0abch
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
    
    mov bx,0
    mov cx,8
s:  push ds:[bx]
    add bx,2
    loop s

    mov bx,0
    mov cx,8
s1: pop ds:[bx]
    add bx,2
    loop s1
    
    mov ax,4c00h
    int 21h
codesg ends
end start
