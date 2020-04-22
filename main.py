import flask
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_login import current_user
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, url_for, flash, redirect, request
import hashlib


print('Illes')