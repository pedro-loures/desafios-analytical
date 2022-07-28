
// function process_image(){
//   const path = '/process_image';
//   document.body.scrollTop = 0; // For Safari
//   document.documentElement.scrollTop = 0;
//   axios.get(path,  {
//     params: {
//       reduce_factor : this.reduce_factor,
//       filter_size : this.filter_size,
//       filter_sensibility : this.filter_sensibility,
//       convolution_factor : this.convolution_factor,
//       padding : this.padding,
//       scan_threshold : this.scan_threshold,
//       vfile : this.vfile,
//     } 
//   })        
//   dragText.textContent = "HERE! ";
// }
var vm = new Vue({
  el: '#image_data',
  data: {
    name: 'Vue.js',
    reduce_factor:7,
    filter_size:10,
    filter_sensibility:15,
    convolution_factor:20,
    padding: 15,
    scan_threshold:0.5,
    image_number: 1,
    image:null
    
  },
  // define methods under the `methods` object
  methods: {
    uploadFile() {
      alert('uploaded')
      this.image = this.$refs.file.files[0];
    },
    process_image: function (event) {
      // `this` inside methods point to the Vue instance

      alert('Hello ' + this.image + '!')
      // `event` is the native DOM event
      const path = '/process_image';  
      document.body.scrollTop = 0; // For Safari
      document.documentElement.scrollTop = 0;
      axios.get(path,  {
        params: {
          reduce_factor : this.reduce_factor,
          filter_size : this.filter_size,
          filter_sensibility : this.filter_sensibility,
          convolution_factor : this.convolution_factor,
          padding : this.padding,
          scan_threshold : this.scan_threshold,
          image_number: this.image_number,
          image : this.image
        } 
      })        
  
      alert(event.target.tagName)
    }
  }
})
// var vm = new Vue({
//   data: {
//     reduce_factor:7,
//     filter_size:10,
//     filter_sensibility:15,
//     convolution_factor:20,
//     padding: 15,
//     scan_threshold:0.5,
//     vfile:file

//   },

  
//   methods: {
//     process_image: function() {
//       dragText.textContent ='função';
//     }
//   }
// });
