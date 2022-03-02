// [rule: ^export (.+)$]

function main(){
    param(1)
    .split("export")
    .flatMap(s=>s.split(" "))
    .filter(s=>s.length>1)
    .map(s=>s.split('=').map(ss=>ss.replace('"','')))
    .forEach(s=>{
        let r=`ql set ${s[0]} ${s[1]}`
        sendText("已转换为: "+r)
        sleep(100)
        breakIn(`ql set ${s[0]} ${s[1]}`)
    })
}

main()