// $(function(){
//     var str = '#len'; //increment by 1 up to 1-nelemnts
//     $(document).ready(function(){
//       var i, stop;
//       i = 1;
//       stop = 4; //num elements
//       setInterval(function(){
//         if (i > stop){
//           return;
//         }
//         $('#len'+(i++)).toggleClass('bounce');
//       }, 500)
//     });
//   });

//   //Function for artist info content change
//   var wholeDiv = document.querySelectorAll('#change');
//   var row1Change = document.querySelectorAll("#row1Change").innerHTML;
//   var row2Change = document.querySelectorAll("#row2Change").innerHTML;
//   var row1Change2 = 'Artist Bio: {{obj.artist_bio}}'

//  function changeInner() {


//  };

// function sucess_modal(){
//   var loading = document.getElementById('loading').innerText
//   var success = document.getElementById('sent-message').innerText
//   var buttonContact = document.getElementById('contact-button').innerText

//   if (buttonContact == 'Send Message') {
//     buttonContact == loading;
//     setTimeout(
//       buttonContact == success, 4000
//     );}
//     else(buttonContact == 'error' );

// setTimeout(document.getElementById('contact-button').submit());



var dialog = document.querySelector('dialog');
dialogPolyfill.registerDialog(dialog);



    
        
      



          function toggleDialog(prefix, index, action) {
            var dialogId = prefix + '-dialog_' + index;
            var dialog = document.getElementById(dialogId);
          
            if (dialog) {
              if (action === 'show') {
                dialog.showModal();
              } else if (action === 'hide') {
                dialog.close();
              }
            }
          }


          