<template>
    <div class="comment-list mt-3">
      <CommentListItem
        v-for="comment in comments"
        :key="comment.id"
        :comment="comment"
      />
      <div v-if="comments?.length===0"><h4>아직 작성된 댓글이 없어요😥</h4></div>
    </div>
</template>
  
<script>
  import CommentListItem from '@/components/CommentListItem'

  export default {
    name: 'CommentList',
    props:{
      comments:Array
    },
    components:{
      CommentListItem
    },
    // computed:{
    //   comments(){
    //     return this.$store.state.comments
    //   }
    // }
  }
</script>

<style>

</style>