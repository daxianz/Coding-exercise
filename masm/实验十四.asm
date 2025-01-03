
assume cs:codesg,ds:datasg,ss:stacksg

datasg segment
    
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

    mov ax,0b800h
    mov es,ax
    mov si,12*160 + 38*2

    mov cx,3
    mov dx,9
    mov dh,0

s:  push cx

    mov al,dl
    dec dx
    out 70h,al
    in al,71h
    
    mov ah,al
    mov cl,4
    shl al,cl
    shr al,cl   ;ax->个位
    shr ah,cl   ;ah->十位
    
    add al,30h  ;转为ASCLL码
    add ah,30h

    
    mov byte ptr es:[si],al
    add si,2
    mov byte ptr es:[si],ah
    add si,2
    mov byte ptr es:[si],'/'
    add si,2

    pop cx
    loop s

    mov byte ptr es:[si],' '
    add si,2

    mov cx,3
    mov dx,4
    mov dh,0

s0:  push cx

    mov al,dl
    sub dx,2
    out 70h,al
    in al,71h
    
    mov ah,al
    mov cl,4
    shl al,cl
    shr al,cl   ;ax->个位
    shr ah,cl   ;ah->十位
    
    add al,30h  ;转为ASCLL码
    add ah,30h

    
    mov byte ptr es:[si],al
    add si,2
    mov byte ptr es:[si],ah
    add si,2
    mov byte ptr es:[si],':'
    add si,2

    pop cx
    loop s0

    mov byte ptr es:[si-2],' '

    mov ax,4c00h
    int 21h
codesg ends
end main
