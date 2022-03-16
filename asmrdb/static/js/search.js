const advanced_button = document.getElementById('toggle_advanced_search')

const advanced_html = `
<!-- If you're working with thsi file, make sure to repaste it back into js/search.js -->
<div id="advanced_search">
  <div id="search_text" class="justify-content-center">
    <h3 class="mt-3">Tags</h3>
    With tags: 
    <input type="text" name="plus_tags" placeholder="+Tags">

    Without tags: 
    <input type="text" name="min_tags" placeholder="-Tags">
  </div>
  <div id="search_classes">
    <h3 class="mt-3">Queries</h3>
    Performer:
    <input type="text" name="performer_query" placeholder="Performer query">
    Audio:
    <input type="text" name="audio_query" placeholder="Audio query">
  </div>
</div>
`;

advanced_button.addEventListener("click", function() {      
    let advanced_info = document.getElementById("advanced_info");
    if ( advanced_info.innerHTML === `` )
    {
        advanced_info.innerHTML = advanced_html;
        document.getElementById("search").required = false;
    } else {
        advanced_info.innerHTML = ``;
        document.getElementById("search").required = true;
    }
});

// const search = document.getElementById('search');
// const matchList = document.getElementById('match-list');

// search.addEventListener('input', () => searchValues(search.value));

// // serach database and filter it
// const searchStates = async searchText => {
//     const res = await fetch('states.json');
//     // all of the states as a javascript object
//     const states = await res.json();

//     // Get matches to current text input
//     let matches = states.filter(state => {
//         const regex = new RegExp(`^${searchText}`, 'gi');
//         // returns either if they match
//         return state.name.match(regex) || state.abbr.match(regex);
//     });

//     // Assuming there's no input, let's not match everything
//     if ( searchText.length === 0  ) {
//         matches = [];
//         matchList.innerHTML = '';
//     }

//     outputHtml(matches);
// }

// // Show results in HTML
// const outputHtml = matches => {
//     if(matches.length > 0){
//         const html = matches.map(match => `
//             <div class="card card-body mb-1">
//                 <h4>
//                     ${match.name} (${match.abbr})
//                     <span class="text-primary">${match.capital}</span>
//                 </h4>
//                 <small>
//                     Lat: ${match.lat} / Long: ${match.long}
//                 </small>
//             </div>
//         `).join('');
//     }

//     matchList.innerHTML = html;
// }

