

function saludar(){

    alert("hola");
}

async function getPokemon(){
    await fetch('https://pokeapi.co/api/v2/pokemon?limit=151')
    .then(response => response.json())
    .then(async res => 
        
        
        await Promise.all(
            res.results.map(
                (pokemon) => getPokemonDetails(pokemon)
          )
        )

        //console.log(res.results)
    )
    .catch((err) => console.log(err));

  };

  async function getPokemonDetails(pokemon){
    
    //console.log(pokemon)
    await fetch(pokemon.url)
    .then(response => response.json())
    //.then(res => console.log ({'name': res.name,'image': res.sprites.front_default} ))
    .then(res => 
        
        
        document.getElementById('wraper').appendChild( buildPokemonCard( {'name': res.name,'image': res.sprites.front_default} ) )
        
        
        //{res.name, res.sprites.front_default} 
    )
    .catch((err) => console.log(err));
  }

  function buildPokemonCard(pokemon){

    var col = document.createElement('div');
    var card = document.createElement('div');
    var cardBody = document.createElement('div');
    var cardTitle = document.createElement('h5');
    var image = document.createElement('img');
    var btn = document.createElement('a');
    
    cardTitle.className = 'card-title';
    cardTitle.innerHTML = pokemon.name;
    cardBody.className = 'card-body';
    cardBody.appendChild(cardTitle);
    btn.href = '#'; 
    btn.className = 'btn btn-primary';
    btn.innerHTML = 'Lo quiero!'; 
    btn.addEventListener('click',() => alert('Proximamente!'));
    cardBody.appendChild(btn);
    image.src = pokemon.image;
    image.className = 'card-img-top';
    image.alt = pokemon.name;
    card.className = 'card';
    card.style = 'width: 18rem;';
    card.appendChild(image);
    card.appendChild(cardBody);
    col.className = 'col';
    col.appendChild(card);

    return col;

    // <div class="col">
    //           <div class="card" style="width: 18rem;">
    //             <img src="..." class="card-img-top" alt="...">
    //             <div class="card-body">
    //               <h5 class="card-title">Card title</h5>
    //               <a href="#" class="btn btn-primary">Go somewhere</a>
    //             </div>
    //           </div>
    //         </div>

  }




  //