from flask import Blueprint, render_template, request
from db import articles_collection
from dto.article import ArticleDTO

# html 파일이 있는 folder path 정의
articles_blueprint = Blueprint("articles_blueprint", __name__, template_folder="../templates/articles")


@articles_blueprint.route("/")
def get_all_articles():
    topic_param = request.args.get("topic")

    filter = {"deleted_at": None}

    if topic_param in ["good", "bad"]:
        filter["topic"] = topic_param
    else:
        topic_param = "all"

    # todo author 를 작성자의 ObjectId 로 설정 후, GET 요청시 lookup 해 오도록 변경
    list_of_articles = list(articles_collection.find(filter))

    # ObjectId 를 문자열로 변환
    for article in list_of_articles:
        article["_id"] = str(article["_id"])

    articles_object = [ArticleDTO.from_dict(article_dict) for article_dict in list_of_articles]

    return render_template('article_list.html', articles=articles_object, topic=topic_param)


@articles_blueprint.route("/", methods=["POST"])
def create_article():
    # 게시물 생성 기능 구현
    return


@articles_blueprint.route("/<string:id>", methods=["DELETE"])
def remove_article():
    # 게시물 삭제 기능 구현
    return


@articles_blueprint.route("/<string:id>", methods=["PATCH"])
def update_article():
    # 게시물 수정 기능 구현
    return


@articles_blueprint.route("/<string:id>")
def get_one_articles(id):
    return render_template('article_detail.html', id=id)


@articles_blueprint.route("/new")
def create_article_page():
    # 게시물 작성 페이지 구현
    return render_template('create_article.html')
