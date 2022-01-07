<template>
    <button class ="button1">
        {{ message }}
    </button>
</template>
<style>
    .button1 {
        box-sizing:border-box;
        padding: 7px;
        padding-top: 5px;
        padding-bottom: 5px;
        width:52px;
        background-color:transparent;
        border-radius: 0.4em;
        border: none;
        color:#000839;
        font-size: 13px;
        cursor: pointer;
    }
    .button1:hover {
        text-decoration: underline;
    }
    .button1:focus {
       text-decoration: underline
    }
</style>
<script>
export default {
  name: 'Button1',
  props: {
    message: String
  }
}
</script>
