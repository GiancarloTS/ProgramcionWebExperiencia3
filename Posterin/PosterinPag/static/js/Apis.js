function getCharacters(done) {

    const results = fetch("https://rickandmortyapi.com/api/character/?name=summer&status=alive");

    results
        .then(response => response.json())
        .then(data => {
            done(data)
        });
}

getCharacters(data => {
    
    data.results.forEach(personaje => {

        const article = document.createRange().createContextualFragment(`
        
        <article>

            <div class="image-container">
                <img src="${personaje.image}">
            </div>

            <h2>${personaje.name}</h2>
            <span>${personaje.status} - ${personaje.species}</span>

        </article>
        `);

        const main = document.querySelector("main");

        main.append(article);
    });
});
