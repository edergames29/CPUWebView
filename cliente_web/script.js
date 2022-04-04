//#Variaveis
let textob = document.getElementById('texto')

let decode = true
let dados = "Nada"
let loop = true
let contagem = 0 //conta as vezes q o pegaurl foi executado



function var_para_dom(txt="Texto não expecificado", classenova) {
    //manda o texto para o html, e tambem a classe se expecificada
    textob.innerHTML = txt
    if (classenova) {
        textob.className = classenova
    }
}

function b64_to_utf8(str) {
    //retorna a string decodificada
    //return decodeURIComponent(escape(window.atob(str))); //Metodo legado
    return decodeURIComponent(window.atob(str));
}

function pegaurl(endereco) {
    const URL_TO_FETCH = 'http://127.0.0.1:8500/admin';
    //quando a funcao callback esta pronta chama varparadom,
    fetch(URL_TO_FETCH, {
            //mode: 'no-cors' // 'cors' by default
        })
        .then(function(response) {
            //console.log(response)
            return response.text();
        }).then(function(data) {
            // This is the JSON from our response
            if (decode) {
                let str = b64_to_utf8(data)
                //String para array
            	//starr = str.split("|")
                console.log(str)
                //pequena correcao para trocar as aspas do json para conseguir converter para objeto
                function formatBytes(a,b=2,k=1024){with(Math){let d=floor(log(a)/log(k));return 0==a?"0 Bytes":parseFloat((a/pow(k,d)).toFixed(max(0,b)))+" "+["Bytes","KB","MB","GB","TB","PB","EB","ZB","YB"][d]}}
                strconv = str
                for(let i=0;i<4;i++){
                    strconv = strconv.replace("'",'"')
                }
                starr = JSON.parse(strconv)
                console.log(strconv)
            	//console.log(starr.count)
                var_para_dom(`Memoria Total:${formatBytes(starr['total'])} | Memoria Usada:${formatBytes(starr['usada'])}`, "notification is-black")
                //console.log(str.split("|")[1])
                
                console.log(contagem)
                
                //condicao para fazer o grafico atualizar apenas duas em duas vezes
                if(contagem >= 2){
                    //ta atualizando o grafico mandando o valor
                    //o split é usado para ir apenas os numeros
                    memoriausada=formatBytes(starr['usada']).split(' ')[0]
                    
                    console.log(memoriausada)
                    atualizadata(memoriausada)
                    contagem=0
                }
                ++contagem
                if (loop) {
                	setTimeout(() => pegaurl(), 2000)
                }
                //contador(2000)
                
                /*
                tempo=1000
                if(ativado == false){
                	console.log('ininciando')
                	iniciar()
                }*/
            }

            //console.log(data);
        })
        .catch(function(err) {
            console.error(err);
            var_para_dom("Erro 404", "notification is-danger")
            console.log("refused")
            if (loop) {
            	setTimeout(() => pegaurl(), 10000)
            }
            
            //clearInterval(intervalo);
            contador(10000)
        });
    console.log(2)
}
/*

let intervalo;
let tempo = 1000
let ativado = false
	function iniciar(parar){
       //Prototipo de loop para pegaurl usando setinterval (deu problemas por causa de stacks em espera).
		if(ativado == false){
			ativado = true
			console.log('iniciou intevalo')
			pegaurl()
			intervalo = setInterval(()=>{
			pegaurl()
			},1000)
		}
	}
*/

//()

//funcao controla apenas a animacao da barra de notificacao
function contador(total=1000){
    //controla a barra de progresso
	console.log('Iniciando contador de progresso.')
	let barra = document.getElementById('barra')
	let inicial=0
	let totalfc=total
	let tempototal = totalfc / 100
	let interbarra = setInterval(()=>{
		++inicial

		barra.value=barra.value+1
		if (barra.value >= 100) {
			console.log('barra parada')
			barra.value=0
			clearInterval(interbarra)
		}
	},tempototal)
}
function desativar() {
    loop=false
    window.alert('Desativado! recarregue a página para reativar.')
}

/* -----------GRAFICO--------------*/
let minino=0;
let mamixo=10;

let arrayprincipal= [1,2,3,4,5,6,7,8,9,10]
var ctx = document.getElementById('myChart').getContext('2d');
var myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: ["-36s","-32s","-28s","-24s","-20s","-16s","-12s","-8s","-4s","Agora"],
        datasets: [{
            label: 'Ram usada',
            data: [1,2,3,4,5,6,7,8,9,10],
            borderWidth: 2,
            borderColor:"black",
            backgroundColor:"#00d1b2",
            fill: true,
            pointBorderRadius:100,
            //cubicInterpolationMode: 'monotone',
            //tension: 0.4
        }]
    },
    options: {
      responsive: true,
        scales: {
            
            y: {
                type:"linear",
                
                /*
                min:minino,
                max:mamixo
                */
                //beginAtZero: false

            },

        }
    }
});
//myChart.data.datasets.data = [100, 200, 300, 400, 500, 600]



//myChart.data.datasets[0].data = arrayprincipal
//setTimeout(()=>myChart.update(),1000)

function atualizadata(valordaram=404) {
    //atualiza o grafico e a array dele.
    arrayprincipal.shift()
    arrayprincipal.push(valordaram)

    myChart.data.datasets[0].data = arrayprincipal
    //minino = arrayprincipal[arrayprincipal.length]-10
    //mamixo = arrayprincipal[arrayprincipal.length]+10
    myChart.update()
}