assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
  db 'Welcome to masm!',0
  db 02h,24h,11000010b
datasg ends


stacksg segment
    dw 8 dup(0)        
stacksg ends

codesg segment
main: 
    mov ax,datasg
    mov ds,ax
    mov ax,stacksg
    mov ss,ax
    mov sp,16

    mov si,07c0h ; 显存偏移地址
    mov di,18 ; 显示的颜色
    mov bx,0 ; 显示的字符

    mov cx,3
s0: call show_str
    add si,160
    add di,1
    mov bx,0
    loop s0

    mov ax,4c00h
    int 21h
 
show_str:
    push ax
    push es
    push cx
    push bx
    push si
    push di

    mov ax,0b800h
    mov es,ax

s:  
    mov cx,0
    mov cl,ds:[bx]
    jcxz ok

    mov al,ds:[bx]
    mov ah,ds:[di]
    mov es:[si],ax
    inc bx
    add si,2
    loop s

ok: pop di
    pop si
    pop bx
    pop cx
    pop es
    pop ax
    ret

codesg ends
end main