;用7ch中断例程完成loop指令的功能
;cx存放循环次数，bx存放s的位移,这个位移是负的
assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    db 8 dup(0)
datasg ends

stacksg segment
    dd 8 dup(0)       
stacksg ends

codesg segment
main: 
    mov ax,stacksg
    mov ss,ax
    mov sp,32
    mov ax,datasg
    mov ds,ax
    mov si,0

    mov ax,0b800h
    mov es,ax
    mov di,160*12

    mov bx,offset s - offset se
    mov cx,80

s:  mov byte ptr es:[di],'!'
    add di,1
    int 7ch
se: nop

lp: push bp
    mov bp,sp
    dec cx
    jcxz ok
    add ss:[bp+2],bx
ok: pop bp
    iret
    mov ax,4c00h
    int 21h

codesg ends
end main