<template>
  <div>
    <div class="border border-dark m-3 me-5 me-5 rounded-2">
        <div class="py-4">
        <h1><router-link  :to="{ name:'MovieDetailView' }">{{comment?.movie.title}}</router-link></h1>
        <!-- <hr>
        <h1>리뷰 제목 : {{comment?.title}}</h1>
        <h3>좋아요한 유저 : {{comment?.like_users}}</h3>
        <h5></h5>
        <h3></h3>
        <h3>좋아요 갯수 : {{comment?.like_users.length}}</h3>
        <button @click="updateComment"> 수정 </button>
        <button @click="deleteComment"> 삭제 </button>
        <h3>리뷰 내용 : {{comment?.content}}</h3>
        <button @click="likeComment">좋아요</button>
        <hr>
        <h5>유저 : {{comment?.user}}</h5>
        <h5>작성 날짜 : {{comment?.created_at}}</h5>
        <h5>수정 날짜 : {{comment?.updated_at}}</h5> -->
        </div>
        <b-card-group deck>
        <b-card footer-tag="footer">
        <h2>리뷰 제목 : {{comment?.title}}</h2>
        <br>
        <b-card-text>
            <h3>리뷰 내용 : {{comment?.content}}</h3><br>
            <h4>작성자 : {{comment?.username}}</h4><br>
            <div @click="likeComment">
                <h3>
                    {{getHeart()}}
                    {{comment?.like_users.length}}
                </h3>
            </div>
            <hr>
        </b-card-text>
        <b-button @click="updateComment" class="me-1"> 수정 </b-button>
        <b-button @click="deleteComment" variant="danger" class="ms-1"> 삭제 </b-button>
        <template #footer>
            <em>
                <h6>작성 날짜 : {{comment?.created_at}}</h6>
                <h6>수정 날짜 : {{comment?.updated_at}}</h6>
            </em>
        </template>
        </b-card>
        </b-card-group>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
import router from '@/router'

const API_URL = "http://127.0.0.1:8000"

export default {
    name: 'CommentDetailView',

    data(){
        return{
            comment : null,
            heart : ["&#128566"]
        }
    },
    created(){
        this.getCommentDetail()
    },
    computed:{
        isLogin(){
            return this.$store.getters.isLogin
        },
    },
    methods:{
        // updateTodoStatus(){
        //     if(this.comment?.like_users)
        // },
        
        getToken: function (){
        const key = this.$store.state.token

        const config = {
            headers:{
                Authorization: `Token ${ key }`
            }
        }
        return config
        },

        getCommentDetail(){
            if(this.isLogin){
               axios({
                method: 'get',
                url: `${API_URL}/main/comment/${this.$route.params.pk}`,
                headers:{
                    Authorization: `Token ${ this.$store.state.token }`
                }
            })
            .then((res)=>{
                console.log(res.data)
                this.comment=res.data
            })
            .catch(err=>console.log(err)) 
            } else {
                alert('로그인이 필요합니다.')
                router.push({ name: "LogInView" })
            }
        },
        updateComment(){
            if(this.comment?.user!==this.$store.state.userInfo){
            alert('본인이 작성한 글만 수정가능합니다.')
            return
        } else{
            router.push({
                name: "CommentUpdateView",
                params:{
                    comment: this.comment
                }
            })
        }
            
        },
        deleteComment(){
            if(this.comment?.user!==this.$store.state.userInfo){
            alert('본인이 작성한 글만 삭제가능합니다.')
            return
        } else{
            const config = this.getToken()

            axios.delete(`${API_URL}/main/comment/${this.$route.params.pk}/`, config)
            //     method: 'delete',
            //     url: `${API_URL}/main/comment/${this.$route.params.pk}`,
            //     headers:{
            //         Authorization: `Token ${ this.$store.state.token }`
            //     },
            // })
            .then((res) => {
                if (res.data.message) {
                    alert("본인 리뷰만 삭제 가능합니다.")
                }
                else {
                    alert('삭제완료!'),
                router.push({ name: "MovieDetailView" })
                }
            }
                
            )
            .catch(err=>console.log(err))
        }
            
            
        },
        likeComment(){
            //현재 게시글에 현재 로그인한 사용자가 좋아요를 누르는 상황
            // 
            // console.log(this.comment)
            // const config = this.getToken()
            
            axios({
                method:'POST',
                url:`${API_URL}/main/comments/${this.comment.id}/like/`,
                headers:{
                    Authorization: `Token ${ this.$store.state.token }`
                }
            })
            .then((res)=>{
                console.log(res.data)
                // console.log(res.data.like_users)
                // console.log(this.comment.like_users.length)
                this.getCommentDetail()
                
                return 

            })
            .catch(error=>{
                console.log(error)
            })
            // axios.get(`${API_URL}/accounts/user/`, config)
            // .then((res) => {
            //     // console.log(res.data.pk)
            //     const userlike = this.comment.like_users
            //     // console.log(userlike)
            //     const usercode = res.data.pk
            //     if (!userlike.includes(usercode)) {
            //         // console.log('제발')
            //         userlike.push(usercode)
            //     }
            //     else {
            //         // console.log('please')
            //         userlike.splice(userlike.indexOf(usercode),1)
            //     }
            // })
        },
        getHeart(){
        if(this.comment?.like_users.includes(this.$store.state.userInfo)===true){
            return this.heart = "😍"
        }else{
            return this.heart = "😶"
        }
      }
    }
}
</script>

<style>

</style>
