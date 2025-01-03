;编写int 9中断例程

assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    dw 0,0
datasg ends

stacksg segment
    dw 16 dup(0)
stacksg ends

codesg segment
main:
    mov ax,datasg
    mov ds,ax
    mov ax,stacksg
    mov ss,ax
    mov sp,32

    cli
    mov ax,0
    mov es,ax
    push es:[9*4]
    pop ds:[0]      ;ip
    push es:[9*4+2]
    pop ds:[2]      ;cs
    sti

    mov word ptr es:[9*4],offset newint9h
    mov es:[9*4+2],cs

    mov ax,0b800h
    mov es,ax
    mov si,12*160 + 39*2
    mov cx,26
    mov ax,0
    mov al,'a'
s: 
    mov es:[si],al
    inc al          ;依次显示'a'到'z'
    call delay       
    loop s

    cli
    mov ax,0
    mov es,ax
    push ds:[0]
    pop es:[9*4]
    push ds:[2]
    pop es:[9*4+2]
    sti
    
    mov ax,4c00h
    int 21h

newint9h:
    push ax
    push bx
    push es

    in al,60h
    
    pushf
    call dword ptr ds:[0]

    mov ah,0
    cmp ax,1
    jne int9ret
    mov ax,0b800h
    mov es,ax
    mov bx,12*160 + 39*2 + 1
    mov al,es:[bx]
    inc al
    mov es:[bx],al

int9ret:
    pop es
    pop bx
    pop ax
    iret

delay:
    push dx
    push ax

    mov dx,10h
    mov ax,0
s0: sub ax,1
    sbb dx,0        ;延时程序
    cmp ax,0
    jne s0
    cmp dx,0
    jne s0

    pop ax
    pop dx
    ret
    
codesg ends
end main
