;安装一个新的int 9中断例程,使得原int 9中断例程的功能得到扩展
;在dos下，按f1键后改变当前屏幕的显示颜色，其他键照常处理

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

    mov ax,0
    mov es,ax       ;保存原int 9中断例程于0:0200单元处
    push es:[9*4]   ;ip
    pop es:[0200h]  
    push es:[9*4+2] ;cs
    pop es:[0200h+2]

    cli
    mov word ptr es:[9*4],0204h ;在向量中断表中设置newint 9的入口地址
    mov word ptr es:[9*4+2],0h
    sti

    mov di,0204h
    push cs
    pop ds             ;将newint 9例程安装到0:0204单元后
    mov si,offset int9ret
    mov cx,offset int9retend - offset int9ret
    cld
    rep movsb

    mov ax,4c00h
    int 21h

newint9h:
    push ax
    push bx
    push cx
    push es

    in al,60h
    
    ;mov cx,0        ;不需要单独设置(cs)=0
    ;mov es,cx       ;当此代码执行时(cs)=0
    pushf           ;调用原有的int 9中断例程
    call dword ptr cs:[0200h]

    mov ah,0
    cmp ax,3bh      
    jne int9ret

    mov ax,0b800h
    mov es,ax
    mov bx,1
    mov cx,25 * 80  ;改变屏幕的显示颜色
s:  inc byte ptr es:[bx]
    add bx,2
    loop s

int9ret:
    pop es
    pop cx
    pop bx
    pop ax
    iret
int9retend:
    nop

delay:
    push dx
    push ax

    mov dx,1000h
    mov ax,0
s0: sub ax,1
    sbb dx,0
    cmp ax,0
    jne s0
    cmp dx,0
    jne s0

    pop ax
    pop dx
    ret

codesg ends
end main
