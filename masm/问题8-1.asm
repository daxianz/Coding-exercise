
assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    dd 100001
    dw 100
    dw 0
datasg ends

stacksg segment
    dw 8 dup(0)
stacksg ends

codesg segment
start: 
    mov ax,datasg
    mov ds,ax
    mov ax,stacksg
    mov ss,ax
    mov sp,16
    mov bx,0

    mov ax,ds:[bx]
    mov dx,ds:[bx+2]
    div word ptr ds:[bx+4]
    mov ds:[bx+6],ax

    mov ax,4c00h
    int 21h
codesg ends

end start
