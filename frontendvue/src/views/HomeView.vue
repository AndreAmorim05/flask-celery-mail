<template>
  <div class="home">
    <img alt="Vue logo" src="../assets/undraw_opened_re_i38e.png">
    <FormsComponent />
    
  </div>
</template>

<script>
// @ is an alias to /src
import FormsComponent from '@/components/FormsComponent.vue'

export default {
  name: 'HomeView',
  components: {
    FormsComponent
  }
}
</script>
