
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

    mov al,8
    out 70h,al
    in al,71h   ;用BCD码表示的月份
    
    mov ah,al
    mov cl,4
    shl al,cl
    shr al,cl   ;ax->个位
    shr ah,cl   ;ah->十位
    
    add al,30h  ;转为ASCLL码
    add ah,30h

    mov ax,0b800h
    mov es,ax
    mov si,12*160 + 39*2
    mov byte ptr es:[si],al
    mov byte ptr es:[si+2],ah

    mov ax,4c00h
    int 21h
codesg ends
end main
