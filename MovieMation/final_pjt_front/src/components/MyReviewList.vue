<template>
  <div>
    <h2>내가 작성한 리뷰들</h2>
    <div class="border border-dark mt-3 ms-5 me-5 rounded-2 py-4" id="overview-scroll3">
    <MyReviewListItem
        v-for="myreview in myreviews"
        :key="myreview.id"
        :myreview="myreview"
    /></div>
  </div>
</template>

<script>
import MyReviewListItem from '@/components/MyReviewListItem'

export default {
    name: 'MyReviewList',
    components:{
        MyReviewListItem,
    },
    props:{
        myreviews:Array
    },
}
</script>

<style>
#overview-scroll3{
  overflow:auto; 
  width:91vw; 
  height:13vw; 
  /* text-align:left; */
  /* background-color: rgb(255, 239, 177); */
  /* margin-left: 15px; */
}
</style>