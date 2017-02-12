<template>
  <div class="hello">
    <h1>{{ msg }}</h1>
    <p>Apparently, this is a Vue.js project :), which is called Progressive JavaScript Framework, seems very interesting. </p>
    <br>
    
    <h2>Here is a list things I intended to force on.(updating...)</h2>
    <ul>
      <li><a href="https://golang.org" target="_blank">Golang</a></li>
      <li><a href="https://vuejs.org" target="_blank">Vue.js</a></li>
      <li><a href="http://grafana.org" target="_blank">Grafana</a></li>
      <li><a href="https://www.rust-lang.org/zh-CN/" target="_blank">Rust</a></li>
    </ul>

    <br>
    <h2>Labs</h2>
    <ul>
      <li><a href="https://github.com/SimonXming/Algorithms-practice" target="_blank">Algorithms-practice</a></li>
      <li><a href="https://blog.comprehend.in" target="_blank">My Blog</a></li>
      <li>暂无</li>
    </ul>
  </div>
</template>

<script>
export default {
  name: 'hello',
  data () {
    return {
      msg: "Welcome to simonshyu's lab."
    }
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
h1, h2 {
  font-weight: normal;
}

ul {
  list-style-type: none;
  padding: 0;
}

li {
  display: inline-block;
  margin: 0 10px;
}

a {
  color: #42b983;
}
</style>
