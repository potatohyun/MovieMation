<template>
    <div>
        <br>
        <h1>404 오류</h1>
        <br>
        <h2>없는 페이지입니다.</h2>
        <h3>하지만 걱정마세요!</h3>
        <h4>영화는 계속됩니다!</h4>
        <button @click="toHome">홈으로</button>
    </div>
    
</template>

<script>
import router from '@/router'

export default {
    
    name : 'FourZeroFourView',
    methods:{
        toHome(){
            router.push({ name: "MovieView" })
        }
    }
    


}
       


</script>

<style>

</style>