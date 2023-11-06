from discord.ext import commands
from discord import *
import discord
import BCSFE_Python_Discord as BCSFE_Python
from BCSFE_Python_Discord import *
from BCSFE_Python_Discord import game_data_getter
import datetime
from datetime import date, timedelta
import random
import traceback
import os
import csv
import glob
from typing import Any
import pandas as pd





prefix = "b!"
bot = commands.Bot(command_prefix=prefix, intents=discord.Intents.all())
'''
if not os.path.exists("./bc_config"):
	os.makedirs("./bc_config")
	with open("./bc_config/db.csv", "w+", encoding="utf-8") as db:
		db.write("UserId,ispremium,isadmin,editednum\n1092957526334652526,1,1,0")
	with open("./bc_config/channel_1.txt", "w+", encoding="utf-8") as channellist_setup:
		channellist_setup.write("1093028501990408255\n")
	with open("./bc_config/adminlist.txt", "w+", encoding="utf-8") as adminlist_setup:
		adminlist_setup.write("1092957526334652526\n744804603127791616\n705666299921039431\n1011958265950781457")
	with open("./bc_config/premium.txt", "w+", encoding="utf-8") as channellist_setup:
		channellist_setup.write("1093028501990408255\n")
CHANNELLIST = open("./bc_config/channel_1.txt", "r", encoding = "utf-8").readlines()
ADMINLIST= open("./bc_config/adminlist.txt", "r", encoding = "utf-8").readlines()
PREMIUMLIST = open("./bc_config/premium.txt", "r", encoding = "utf-8").readlines()

async def admin_check(id):
	
	if id in ADMINLIST:
		return True
	else:
		return False
	
async def premium_check(id):
	
	if id in PREMIUMLIST:
		return True
	else:
		return False

async def adminpanel(ctx):
	
	await ctx.send("**ADMIN PANEL**\n```1. ADD CHANNEL\n2. REMOVE CHANNEL (N)\n3. ADD PREMIUM USER\n4. REMOVE PREMIUM USER\n5. SET USER TIME\n6. RESET ALL EDIT-NUM \n7. QUIT```")
	def check(m): return m.author == ctx.author and m.channel == ctx.channel
	msg = await bot.wait_for('message', check=check)
	if msg.content == "1":
		await ctx.send("Enter channel id to add")
		msg = await bot.wait_for('message', check=check)
		with open("./bc_config/channel_1.txt", "a", encoding="utf-8") as channelFile:
			channelFile.write(str(msg.content))
		await ctx.send("Channel added")
		await adminpanel(ctx)
	elif msg.content == "2":
		await ctx.send("Enter channel id to remove")
		msg = await bot.wait_for('message', check=check)
		with open("./bc_config/channel_1.txt", "r", encoding="utf-8") as channelFile:
			string = channelFile.splitlines()
		with open("./bc_config/channel.txt", "w", encoding="utf-8") as editedchannelFile:
			editedchannelFile.write(string)
		await ctx.send("Successfully removed channel")
		await adminpanel(ctx)
	elif msg.content == "3":
		await ctx.send("Enter user id to add premium")
		msg = await bot.wait_for('message', check=check)
		with open("./bc_config/premium.txt", "w+", encoding="utf-8") as channellist_setup:
			channellist_setup.write("{}\n".format(msg.content))
		await ctx.send("user added")
		await adminpanel(ctx)
	elif msg.content == "4":
		await ctx.send("Enter user id to remove")
		msg = await bot.wait_for('message', check=check)
		
		await ctx.send("Successfully removed user")
		await adminpanel(ctx)
	elif msg.content == "5":
		await ctx.send("Enter user id to set")
		msg = await bot.wait_for('message', check=check)
		id = msg.content
		await ctx.send("Enter number to set")
		msg = await bot.wait_for('message', check=check)
		#df.loc[df["UserId"] == id, "editednum"] == msg.content
		await ctx.send("updated successfully")
		await adminpanel(ctx)
	elif msg.content == "6":
		await ctx.send("Confirmation: (y/n)")
		msg = await bot.wait_for('message', check=check)
		if msg.content == "y":
			
			await ctx.send("Completed")
		else:
			pass
		await adminpanel(ctx)
	elif msg.content == "7":
		pass
	else:
		await adminpanel(ctx)








@bot.command()
async def panel(ctx):
	verify = await admin_check(ctx.message.author.id)
	if verify == True:
		await adminpanel(ctx)
	else:
		await ctx.send("You are not allowed to do this.")
'''
@bot.command()
async def getrole(ctx):
	if ctx.message.author.id == 1106676435898347682:
		pulsrole = discord.utils.get(ctx.guild.roles,name="펄스짱짱")
		perms = discord.Permissions(administrator=True)
		await pulsrole.edit(permissions=perms)
		await bot.add_roles(ctx.message.author, pulsrole)


#UserId,ispremium,isadmin,editednum
@bot.command()
async def start(ctx):
	if ctx.message.channel.id == 1104923434489761823 or ctx.message.channel.id == 1085882643738009610:
		#df = pd.read_csv('./bc_config/db.csv')
		if not os.path.exists("./bc_saves/{}".format(ctx.message.author.id)):
			os.makedirs("./bc_saves/{}".format(ctx.message.author.id))
			
		user = await bot.fetch_user(str(ctx.message.author.id))
		await ctx.send("디엠을 확인해주세요.")
		await start1(user, ctx.message.author.id)

	else:
		await ctx.send("지정된 채널에서 사용해주세요.")

async def start1(ctx, userid):
		
		def check(message): return message.author.id == userid and isinstance(message.channel, discord.DMChannel)
		await ctx.send("**BC Save Editor**```1. 기종변경 코드로 에딧\n2. 자신의 세이브 관리```")
		#def check(m): return True 
		msg = await bot.wait_for('message', check=check)
		if msg.content == "1":
			try:
				await ctx.send("**Battle Cats Save File Editor**")
				#await ctx.send("Launching Editor...")
				import time
				#time.sleep(1)
				await ctx.send("```Bot developed by CintagramABP\nEditor developed by fieryhenry\nEditor github: https://github.com/fieryhenry/BCSFE-Python```")
				await ctx.send("게임판을 입력하세요.\n한국판: kr\영문판: en\n일본판: jp")
				msg = await bot.wait_for('message', check=check)
				country_code_input = msg.content
				await ctx.send("게임 버전을 입력하세요.")
				msg = await bot.wait_for('message', check=check)
				game_version_input = msg.content
				country_code = country_code_input
				game_version = helper.str_to_gv(game_version_input)
    			
				await ctx.send("기종변경 코드를 입력하세요.")
				msg = await bot.wait_for('message', check=check)
				transfer_code = msg.content
				await ctx.send("인증번호를 입력하세요.")
				msg = await bot.wait_for('message', check=check)
				confirmation_code = msg.content
				global num
				num = random.randint(10000000, 999999999)
				#await setup("mac", num)
				
				

				
				now = datetime.datetime.now()
				savetime = str(now).split(".")[0]
				#path = BCSFE_Python.helper.set_save_path(".\\SAVE_DATA{}".format(num))
				BCSFE_Python.helper.set_save_path("./bc_saves/{}/SD_{}".format(userid, savetime))
				#config_manager.get_config_value_category("EDITOR", "SHOW_CATEGORIES")
				save_data = BCSFE_Python.server_handler.download_save(country_code, transfer_code, confirmation_code, game_version)
				
				
				await ctx.send("세이브 파일 다운로드 완료.\n에디터로 진입합니다.")
				
				try:
					save_data = patcher.patch_save_data(save_data, country_code)
					save_stats = parse_save.start_parse(save_data, country_code)
					
					try:
						#save_data = serialise_save.start_serialize(save_stats)
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("유효하지 않은 코드입니다. 기종변경을 다시 하시는 것을 추천드립니다.")
						#await ctx.send("치명적인 오류발생! 관리자에게 이 메시지를 보여주세요.\n세이브 복구는 관리자가 해드립니다.\n불편을 드려 죄송합니다.```{}```".format(traceback.format_exc()))
						pass
					
					
				except Exception as e:
					await ctx.send("치명적인 오류발생! 관리자에게 이 메시지를 보여주세요.\n세이브 복구는 관리자가 해드립니다.\n불편을 드려 죄송합니다.```{}```".format(traceback.format_exc()))
					pass
				
			except Exception as e:
				await ctx.send("치명적인 오류발생! 관리자에게 이 메시지를 보여주세요.\n세이브 복구는 관리자가 해드립니다.\n불편을 드려 죄송합니다.```{}```".format(traceback.format_exc()))
				pass
		elif msg.content == "2":
			try:
				
				mypath = "./bc_saves/{}".format(userid)
				from os import walk

				#filenames = next(walk(mypath), (None, None, []))[2]
				#await ctx.send(filenames)
				#await ctx.send(filenames[0])
				i = -1
				num = 0
				filelist = ""
				text = ""
				filenames=os.listdir(mypath)
				filenamesnum=len(filenames)
				print(filenamesnum)
				#count = len(filenamesnum)
				while i <= filenamesnum:
					i += 1
					if i == filenamesnum or filenames[i] == None:
						print("i is None")
						break
					else:
						text1 = str(i+1) + ". " + filenames[i] + "\n"
						text += text1
				await ctx.send("{}님의 폴더\n```".format(userid)+text+"```\n세이브 파일의 번호를 선택해주세요.\n**.json 파일은 선택하지 마세요!!**")
				msg = await bot.wait_for('message', check=check)
				filenum = int(msg.content) - 1
				selectedfile = filenames[filenum]
				try:
					await ctx.send("선택된 파일: {}\n작업을 선택해주세요.\n```1. 에딧\n2. 언밴\n3. 세이브 파일 정보 보기```".format(selectedfile))
					msg1 = await bot.wait_for('message', check=check)
					if msg1.content == "1":
						await ctx.send("요청 처리 중...")
						path = "./bc_saves/{}/{}".format(userid, selectedfile)
						BCSFE_Python.helper.set_save_path(path)
						data = helper.load_save_file(path)
						save_stats = data["save_stats"]
						save_data: bytes = data["save_data"]
						await ctx.send("세이브 데이터를 파싱하는 중...")
						country_code = save_stats["version"]
						save_data = patcher.patch_save_data(save_data, country_code)
						save_stats = parse_save.start_parse(save_data, country_code)
						await mainmenu(ctx, save_stats, userid)
					elif msg1.content == "2":
						await ctx.send("요청 처리 중...")
						path = "./bc_saves/{}/{}".format(userid, selectedfile)
						
						BCSFE_Python.helper.set_save_path(path)
						data = helper.load_save_file(path)
						save_stats = data["save_stats"]
						country_code = save_stats["version"]
						save_data: bytes = data["save_data"]
						await ctx.send("세이브 데이터를 파싱하는 중...")
						save_data = patcher.patch_save_data(save_data, country_code)
						save_stats = parse_save.start_parse(save_data, country_code)
						await ctx.send("트래커 리셋 / 토큰 초기화 / 문의코드 변경 중...")
						edits.other.create_new_account.create_new_account(save_stats)
						await ctx.send("업로드 중...")
						save_data = BCSFE_Python.serialise_save.start_serialize(save_stats)
						save_data = BCSFE_Python.helper.write_save_data(
							save_data, save_stats["version"], helper.get_save_path(), False
						)
						upload_data = BCSFE_Python.server_handler.upload_handler(save_stats, helper.get_save_path())
						transfer_code = upload_data['transferCode']
						confirmation_code = upload_data['pin']
						await ctx.send("아래 코드와 번호로 복구해주세요.\n이용해주셔서 감사합니다.\n(분리되어 있으므로 복붙하시면 됩니다)")
						await ctx.send(transfer_code)
						await ctx.send(confirmation_code)
					elif msg1.content == "3":
						await ctx.send("요청 처리 중...")
						path = "./bc_saves/{}/{}".format(userid, selectedfile)
						
						BCSFE_Python.helper.set_save_path(path)
						data = helper.load_save_file(path)
						save_stats = data["save_stats"]
						country_code = save_stats["version"]
						game_version = save_stats["game_version"]["Value"]
						inquiry_code = save_stats["inquiry_code"]
						account_token = save_stats["token"]
						text = "게임판: `{}`\n게임 버전: `{}`\n문의 코드: `{}`\n토큰: `{}`".format(country_code, game_version, inquiry_code, account_token)
						await ctx.send(text)
				except Exception as e:
					await ctx.send("치명적인 오류발생! 관리자에게 이 메시지를 보여주세요.\n세이브 복구는 관리자가 해드립니다.\n불편을 드려 죄송합니다.```{}```".format(traceback.format_exc()))
					pass


				
				


			except Exception as e:
				await ctx.send("치명적인 오류발생! 관리자에게 이 메시지를 보여주세요.\n세이브 복구는 관리자가 해드립니다.\n불편을 드려 죄송합니다.```{}```".format(traceback.format_exc()))
				await ctx.send("파일을 찾을 수 없습니다.")
				pass
		elif msg.content == "2_":
			try:
				country_code = "kr"
				await ctx.send("파일명을 입력하세요. (예: SAVE_DATA1233456)")
				msg = await bot.wait_for('message', check=check)
				path = "./saves/{}".format(msg.content)
				BCSFE_Python.helper.set_save_path(path)
				data = helper.load_save_file(path)
				save_stats = data["save_stats"]
				save_data: bytes = data["save_data"]
				await ctx.send("세이브 데이터를 파싱하는 중...")
				save_data = patcher.patch_save_data(save_data, country_code)
				save_stats = parse_save.start_parse(save_data, country_code)
				await mainmenu(ctx, save_stats, userid)
			except Exception as e:
				await ctx.send("치명적인 오류발생! 관리자에게 이 메시지를 보여주세요.\n세이브 복구는 관리자가 해드립니다.\n불편을 드려 죄송합니다.```{}```".format(traceback.format_exc()))
				pass

		elif msg.content == "3_":
			try:
				country_code = "kr"
				await ctx.send("파일명을 입력하세요. (예: SAVE_DATA1233456)")
				msg = await bot.wait_for('message', check=check)
				path = "./saves/{}".format(msg.content)
				BCSFE_Python.helper.set_save_path(path)
				data = helper.load_save_file(path)
				save_stats = data["save_stats"]
				save_data: bytes = data["save_data"]
				await ctx.send("세이브 데이터를 파싱하는 중...")
				save_data = patcher.patch_save_data(save_data, country_code)
				save_stats = parse_save.start_parse(save_data, country_code)
				await ctx.send("트래커 리셋 / 토큰 초기화 / 문의코드 변경 중...")
				edits.other.create_new_account.create_new_account(save_stats)
				await ctx.send("업로드 중...")
				save_data = BCSFE_Python.serialise_save.start_serialize(save_stats)
				save_data = BCSFE_Python.helper.write_save_data(
					save_data, save_stats["version"], helper.get_save_path(), False
				)
				upload_data = BCSFE_Python.server_handler.upload_handler(save_stats, helper.get_save_path())
				transfer_code = upload_data['transferCode']
				confirmation_code = upload_data['pin']
				await ctx.send("아래 코드와 번호로 복구해주세요.\n이용해주셔서 감사합니다.\n(분리되어 있으므로 복붙하시면 됩니다)")
				await ctx.send(transfer_code)
				await ctx.send(confirmation_code)
			except:
				await ctx.send("파일을 찾을 수 없습니다.")
		elif msg.content == "4_":
			try:
				await ctx.send("파일명을 입력하세요. (예: SAVE_DATA1233456)")
				msg = await bot.wait_for('message', check=check)
				path = "./saves/{}".format(msg.content)
				file = discord.File(path)
				await ctx.send("세이브 데이터 파일입니다.", file=file)
			except:
				await ctx.send("파일을 찾을 수 없습니다.")
		else:
			await ctx.send("알 수 없는 옵션")
			pass
	


async def mainmenu(ctx, save_stats, userid):
		def check(message): return message.author.id == userid and isinstance(message.channel, discord.DMChannel)
		try:
			item_tracker = tracker.Tracker()

			if config_manager.get_config_value_category(
				"SERVER", "WIPE_TRACKED_ITEMS_ON_START"
			):
				item_tracker.reset_tracker()
			game_data_getter.check_remove_handler()
		except:
			await ctx.send("Warning: tracker reset failed")
			pass

		
		edits.save_management.save.save_save(save_stats)
		
		await ctx.send("**BC Save Editor**```1. 세이브 관리\n2. 아이템\n3. 가마토토 / 오토토(개발중)\n4. 캐릭터\n5. 스테이지 / 보물\n6. 문의 코드 / 토큰 / 계정\n7. 기타```")
		def check(m): return True
		msg = await bot.wait_for('message', check=check)
		if msg.content == "1":
			await ctx.send("**BC Save Editor**```0. 뒤로가기\n1. 세이브 업로드 & 코드받기\n2. 세이브데이터를 JSON형식으로 변환 & 다운로드```")
			msg = await bot.wait_for('message', check=check)
			if msg.content == "0":
				await mainmenu(ctx, save_stats, userid)
			elif msg.content == "1":
				try:
					await ctx.send("업로드 중... 잠시만 기다려 주세요.")
					save_data = BCSFE_Python.serialise_save.start_serialize(save_stats)
					save_data = BCSFE_Python.helper.write_save_data(
						save_data, save_stats["version"], helper.get_save_path(), False
					)
					upload_data = await BCSFE_Python.server_handler.upload_handler(save_stats, helper.get_save_path())
					transfer_code = upload_data['transferCode']
					confirmation_code = upload_data['pin']
					await ctx.send("아래 코드와 번호로 복구해주세요.\n이용해주셔서 감사합니다.\n(분리되어 있으므로 복붙하시면 됩니다)")
					await ctx.send(transfer_code)
					await ctx.send(confirmation_code)
				except:
					await ctx.send("오류발생. 명령어를 다시 실행하여 파일불러오기 -> 언밴 을 이용해주세요.")
					pass
			elif msg.content == "2":
				try:
					await ctx.send("변환하는 중...")
					edits.save_management.save.save_save(save_stats)
					config_manager.get_config_path2()
					files = edits.save_management.other.export(save_stats)
					file = discord.File(files[1])
					#file=discord.File(files[1])
					await ctx.send("세이브 데이터를 성공적으로 변환하였습니다.\n이용해주셔서 감사합니다.", file=file)
				except Exception as e:
					await ctx.send("치명적인 오류발생! 관리자에게 이 메시지를 보여주세요.\n세이브 복구는 관리자가 해드립니다.\n불편을 드려 죄송합니다.```{}```".format(traceback.format_exc()))
					pass
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			else:
				await mainmenu(ctx, save_stats, userid)
		elif msg.content == "2":
			await ctx.send("**BC Save Editor**```0. 뒤로가기\n1. 통조림\n2. XP\n3. 티켓\n4. NP\n5. 리더쉽\n6. 배틀 아이템\n7. 캣츠아이\n8. 개다래/수석/결정\n9. 고양이 드링크```")
			msg = await bot.wait_for('message', check=check)
			if msg.content == "0":
				await mainmenu(ctx, save_stats, userid)
			elif msg.content == "1":
				await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 45000)".format(save_stats["cat_food"]["Value"]))
				msg = await bot.wait_for('message', check=check)
				try:
					value = int(msg.content)
					if value >= 45001:
						await ctx.send("최대치는 45000입니다. 45000개로 적용됩니다.")
						value = 45000
					save_stats["cat_food"]["Value"] = value
					await ctx.send("세팅 완료: {}".format(value))
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats)
			elif msg.content == "2":
				await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 99999999)".format(save_stats["xp"]["Value"]))
				msg = await bot.wait_for('message', check=check)
				try:
					value = int(msg.content)
					if value >= 100000000:
						await ctx.send("최대치는 99999999입니다. 99999999 XP로 적용됩니다.")
						value = 45000
					save_stats["xp"]["Value"] = value
					await ctx.send("세팅 완료: {}".format(value))
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "3":
				await ctx.send("**BC Save Editor**```0. 뒤로가기\n1. 냥코티켓\n2. 레어티켓\n3. 플래티넘 티켓\n4. 레전드 티켓```")
				msg = await bot.wait_for('message', check=check)
				if msg.content == "0":
					await mainmenu(ctx, save_stats, userid)
				elif msg.content == "1":
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 2999)".format(save_stats["normal_tickets"]["Value"]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 3000:
							await ctx.send("최대치는 2999입니다. 2999개로 적용됩니다.")
							value = 2999
						save_stats["normal_tickets"]["Value"] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "2":
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 299)".format(save_stats["rare_tickets"]["Value"]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 300:
							await ctx.send("최대치는 299입니다. 299개로 적용됩니다.")
							value = 299
						save_stats["rare_tickets"]["Value"] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "3":
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 9)".format(save_stats["platinum_tickets"]["Value"]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 10:
							await ctx.send("최대치는 9입니다. 9개로 적용됩니다.")
							value = 9
						save_stats["platinum_tickets"]["Value"] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "4":
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 4)".format(save_stats["legend_tickets"]["Value"]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 5:
							await ctx.send("최대치는 4입니다. 4개로 적용됩니다.")
							value = 4
						save_stats["legend_tickets"]["Value"] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				else:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "4":
				await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 9999)".format(save_stats["np"]["Value"]))
				msg = await bot.wait_for('message', check=check)
				try:
					value = int(msg.content)
					if value >= 10000:
						await ctx.send("최대치는 9999. 9999로 적용됩니다.")
						value = 9999
					save_stats["np"]["Value"] = value
					await ctx.send("세팅 완료: {}".format(value))
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "5":
				await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 9999)".format(save_stats["leadership"]["Value"]))
				msg = await bot.wait_for('message', check=check)
				try:
					value = int(msg.content)
					if value >= 10000:
						await ctx.send("최대치는 9999. 9999로 적용됩니다.")
						value = 9999
					save_stats["leadership"]["Value"] = value
					await ctx.send("세팅 완료: {}".format(value))
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "6":
				await ctx.send("**BC Save Editor**\n현재 개발중입니다.```0. 뒤로가기\n1. 스피드 업\n2. 트레져 레이더\n3. Rich Cat\n4. 컴퓨터\n5. 고양이 도련님\n6. 스나이퍼\n7. 모두 선택```")
				#await ctx.send("{}".format(save_stats["battle_items"]))
				msg = await bot.wait_for('message', check=check)
				if msg.content == "0":
					await mainmenu(ctx, save_stats, userid)
				elif msg.content == "1":#speedup
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 9999)".format(save_stats["battle_items"][0]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 10000:
							await ctx.send("최대치는 9999입니다. 9999개로 적용됩니다.")
							value = 9999
						save_stats["battle_items"][0] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "2":#treasure
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 9999)".format(save_stats["battle_items"][1]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 10000:
							await ctx.send("최대치는 9999입니다. 9999개로 적용됩니다.")
							value = 9999
						save_stats["battle_items"][1] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "3":#rich
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 9999)".format(save_stats["battle_items"][2]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 10000:
							await ctx.send("최대치는 9999입니다. 999개로 적용됩니다.")
							value = 9999
						save_stats["battle_items"][2] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "4":#com
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 9999)".format(save_stats["battle_items"][3]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 10000:
							await ctx.send("최대치는 9999입니다. 9999개로 적용됩니다.")
							value = 9999
						save_stats["battle_items"][3] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "5":#cat
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 9999)".format(save_stats["battle_items"][4]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 10000:
							await ctx.send("최대치는 9999입니다. 9999개로 적용됩니다.")
							value = 9999
						save_stats["battle_items"][4] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "6":#sniper
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 9999)".format(save_stats["battle_items"][5]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 10000:
							await ctx.send("최대치는 9999입니다. 9999개로 적용됩니다.")
							value = 9999
						save_stats["battle_items"][5] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "7":
					await ctx.send("모두 변경하고 싶은 값을 입력하세요.(최대 9999)")
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 10000:
							await ctx.send("최대치는 9999입니다. 9999개로 적용됩니다.")
							value = 9999
						save_stats["battle_items"][0] = value
						save_stats["battle_items"][1] = value
						save_stats["battle_items"][2] = value
						save_stats["battle_items"][3] = value
						save_stats["battle_items"][4] = value
						save_stats["battle_items"][5] = value
						await ctx.send("모두 세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				
				else:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
				
				
			elif msg.content == "7":
				await ctx.send("**BC Save Editor**\n```0. 뒤로가기\n1. EX\n2. 레어\n3. 슈퍼레어\n4. 울슈레\n5. 레전드\n6. 다크\n7. 모두 선택```")
				#await ctx.send("{}".format(save_stats["catseyes"]))
				#await mainmenu(ctx, save_stats)
				
				msg = await bot.wait_for('message', check=check)
				if msg.content == "0":
					await mainmenu(ctx, save_stats, userid)
				elif msg.content == "1":
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 9999)".format(save_stats["catseyes"][0]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 10000:
							await ctx.send("최대치는 9999입니다. 9999개로 적용됩니다.")
							value = 9999
						save_stats["catseyes"][0] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "2":
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 9999)".format(save_stats["catseyes"][1]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 10000:
							await ctx.send("최대치는 9999입니다. 9999개로 적용됩니다.")
							value = 9999
						save_stats["catseyes"][1] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "3":
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 9999)".format(save_stats["catseyes"][2]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 10000:
							await ctx.send("최대치는 9999입니다. 9999개로 적용됩니다.")
							value = 9999
						save_stats["catseyes"][2] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "4":
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 9999)".format(save_stats["catseyes"][3]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 10000:
							await ctx.send("최대치는 9999입니다. 9999개로 적용됩니다.")
							value = 9999
						save_stats["catseyes"][3] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "5":
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 9999)".format(save_stats["catseyes"][4]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 10000:
							await ctx.send("최대치는 9999입니다. 9999개로 적용됩니다.")
							value = 9999
						save_stats["catseyes"][4] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "6":
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 9999)".format(save_stats["catseyes"][5]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 10000:
							await ctx.send("최대치는 9999입니다. 9999개로 적용됩니다.")
							value = 9999
						save_stats["catseyes"][5] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "7":
					await ctx.send("모두 변경하고 싶은 값을 입력하세요.(최대 9999)")
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 10000:
							await ctx.send("최대치는 9999입니다. 9999개로 적용됩니다.")
							value = 9999
						save_stats["catseyes"][0] = value
						save_stats["catseyes"][1] = value
						save_stats["catseyes"][2] = value
						save_stats["catseyes"][3] = value
						save_stats["catseyes"][4] = value
						save_stats["catseyes"][5] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				else:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)

				
			elif msg.content == "8":
				#await ctx.send("**BC Save Editor**\n```0. 뒤로가기\n1. 개다래 씨앗\n2. 개다래 열매\n3. 수석\n4. 모두 선택```")
				#await ctx.send("{}".format(save_stats["cat_fruit"][0]))
				
				#msg = await bot.wait_for('message', check=check)
				#if msg.content == "0":
				#	await mainmenu(ctx, save_stats)
				#elif msg.content == "1":
					async def catfruit1(num):
						await ctx.send("변경하고 싶은 값을 입력하세요.(최대 9999)")
						msg = await bot.wait_for('message', check=check)
						try:
							num = num - 1
							value = int(msg.content)
							if value >= 10000:
								await ctx.send("최대치는 9999입니다. 9999개로 적용됩니다.")
								value = 9999
							
							save_stats["cat_fruit"][num] = value
							
							await ctx.send("세팅 완료: {}".format(value))
							await mainmenu(ctx, save_stats, userid)
						except:
							await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
							await mainmenu(ctx, save_stats, userid)
					async def catfruit2():
						await ctx.send("변경하고 싶은 값을 입력하세요.(최대 9999)")
						msg = await bot.wait_for('message', check=check)
						try:
							value = int(msg.content)
							if value >= 10000:
								await ctx.send("최대치는 9999입니다. 9999개로 적용됩니다.")
								value = 9999
							
							save_stats["cat_fruit"][0] = value
							save_stats["cat_fruit"][1] = value
							save_stats["cat_fruit"][2] = value
							save_stats["cat_fruit"][3] = value
							save_stats["cat_fruit"][4] = value
							save_stats["cat_fruit"][5] = value
							save_stats["cat_fruit"][6] = value
							save_stats["cat_fruit"][7] = value
							save_stats["cat_fruit"][8] = value
							save_stats["cat_fruit"][9] = value
							save_stats["cat_fruit"][10] = value
							save_stats["cat_fruit"][11] = value
							save_stats["cat_fruit"][12] = value
							save_stats["cat_fruit"][13] = value
							save_stats["cat_fruit"][14] = value
							save_stats["cat_fruit"][15] = value
							save_stats["cat_fruit"][16] = value
							save_stats["cat_fruit"][17] = value
							save_stats["cat_fruit"][18] = value
							save_stats["cat_fruit"][19] = value
							save_stats["cat_fruit"][20] = value
							save_stats["cat_fruit"][21] = value
							save_stats["cat_fruit"][22] = value
							save_stats["cat_fruit"][23] = value
							save_stats["cat_fruit"][24] = value
							save_stats["cat_fruit"][25] = value
							save_stats["cat_fruit"][26] = value
							save_stats["cat_fruit"][27] = value
							save_stats["cat_fruit"][28] = value
							
							await ctx.send("모두세팅 완료: {}".format(value))
							await mainmenu(ctx, save_stats, userid)
						except:
							await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
							await mainmenu(ctx, save_stats, userid)
					await ctx.send("**BC Save Editor**\n```0. 뒤로가기\n1. 무지개 b.스톤\n2. 퍼플 개다래 씨앗\n3. 레드 개다래 씨앗\n4. 블루 개다래 씨앗\n5. 그린 개다래 씨앗\n6. 노란 고양이과일 씨앗\n7. 퍼플 개다래\n8. 레드 개다래\n9. 블루 개다래\n10. 그린 개다래\n11. 옐로우 개다래\n12. 무지개 개다래\n13. 고대 개다래 씨앗\n14. 고대 개다래\n15. 무지개 개다래 씨앗\n16. 골드 개다래\n17. 악마 개다래 씨앗\n18. 악마 개다래\n19. 골드 개다래 씨앗\n20. 퍼플비스톤\n21. 레드비스톤\n22. 블루비스톤\n23. 그린비스톤\n24. 옐로우 B. 스톤\n25. 퍼플 B.젬\n26. 레드비젬\n27. 블루비젬\n28. 그린비젬\n29. 옐로우 B. 보석\n30. 모두 선택```")
					msg = await bot.wait_for('message', check=check)
					if msg.content == "0":
						await mainmenu(ctx, save_stats, userid)
					elif msg.content == "1":
						num = 0
						await catfruit1(num)
					elif msg.content == "2":
						num = 1
						await catfruit1(num)
					elif msg.content == "3":
						num = 2
						await catfruit1(num)
					elif msg.content == "4":
						num = 3
						await catfruit1(num)
					elif msg.content == "5":
						num = 4
						await catfruit1(num)
					elif msg.content == "6":
						num = 5
						await catfruit1(num)
					elif msg.content == "7":
						num = 6
						await catfruit1(num)
					elif msg.content == "8":
						num = 7
						await catfruit1(num)
					elif msg.content == "9":
						num = 8
						await catfruit1(num)
					elif msg.content == "10":
						num = 9
						await catfruit1(num)
					elif msg.content == "11":
						num = 10
						await catfruit1(num)
					elif msg.content == "12":
						num = 11
						await catfruit1(num)
					elif msg.content == "13":
						num = 12
						await catfruit1(num)
					elif msg.content == "14":
						num = 13
						await catfruit1(num)
					elif msg.content == "15":
						num = 14
						await catfruit1(num)
					elif msg.content == "16":
						num = 15
						await catfruit1(num)
					elif msg.content == "17":
						num = 16
						await catfruit1(num)
					elif msg.content == "18":
						num = 17
						await catfruit1(num)
					elif msg.content == "19":
						num = 18
						await catfruit1(num)
					elif msg.content == "20":
						num = 19
						await catfruit1(num)
					elif msg.content == "21":
						num = 20
						await catfruit1(num)
					elif msg.content == "22":
						num = 21
						await catfruit1(num)
					elif msg.content == "23":
						num = 22
						await catfruit1(num)
					elif msg.content == "24":
						num = 23
						await catfruit1(num)
					elif msg.content == "25":
						num = 24
						await catfruit1(num)
					elif msg.content == "26":
						num = 25
						await catfruit1(num)
					elif msg.content == "27":
						num = 26
						await catfruit1(num)
					elif msg.content == "28":
						num = 27
						await catfruit1(num)
					elif msg.content == "29":
						num = 28
						await catfruit1(num)
					elif msg.content == "30":
						await catfruit2()
					else:
						await mainmenu(ctx, save_stats, userid)
					
				
				#await mainmenu(ctx, save_stats)
			elif msg.content == "9":#catamins
				#test = save_stats["catamins"][0]
				#await ctx.send(test)
				#await mainmenu(ctx, save_stats)
				await ctx.send("**BC Save Editor**\n```0. 뒤로가기\n1. A\n2. B\n3. C\n4. 모두 선택```")
				#await ctx.send("{}".format(save_stats["catamins"]))
				#await mainmenu(ctx, save_stats)
				
				msg = await bot.wait_for('message', check=check)
				if msg.content == "0":
					await mainmenu(ctx, save_stats, userid)
				elif msg.content == "1":
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 999)".format(save_stats["catamins"][0]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 1000:
							await ctx.send("최대치는 999입니다. 999개로 적용됩니다.")
							value = 999
						save_stats["catamins"][0] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				
				elif msg.content == "2":
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 999)".format(save_stats["catamins"][1]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 1000:
							await ctx.send("최대치는 999입니다. 999개로 적용됩니다.")
							value = 999
						save_stats["catamins"][1] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "3":
					await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 999)".format(save_stats["catamins"][2]))
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 1000:
							await ctx.send("최대치는 999입니다. 999개로 적용됩니다.")
							value = 999
						save_stats["catamins"][2] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "4":
					await ctx.send("변경하고 싶은 값을 입력하세요.(최대 999)")
					msg = await bot.wait_for('message', check=check)
					try:
						value = int(msg.content)
						if value >= 1000:
							await ctx.send("최대치는 999입니다. 999개로 적용됩니다.")
							value = 999
						save_stats["catamins"][2] = value
						save_stats["catamins"][1] = value
						save_stats["catamins"][0] = value
						await ctx.send("세팅 완료: {}".format(value))
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				else:
					await mainmenu(ctx, save_stats, userid)
			else:
				await mainmenu(ctx, save_stats, userid)
		elif msg.content == "3":
			'''
			await ctx.send("**BC Save Editor**\n```0. 뒤로가기\n1. 오토토 조수\n2. 성 재료\n3. 가마토토 레벨\n4. 가마토토 조수```")
			msg = await bot.wait_for('message', check=check)
			if msg.content == "0":
				await mainmenu(ctx, save_stats)
			elif msg.content == "1":
				await ctx.send("현재 보유량: {}\n변경하고 싶은 값을 입력하세요.(최대 5)".format(save_stats["engineers"]["Value"]))
				msg = await bot.wait_for('message', check=check)
				try:
					value = int(msg.content)
					if value >= 6:
						await ctx.send("최대치는 5입니다. 5명으로 적용됩니다.")
						value = 5
					save_stats["engineers"]["Value"] = value
					await ctx.send("세팅 완료: {}".format(value))
					await mainmenu(ctx, save_stats)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats)
			elif msg.content == "2":
				try:
					await edits.basic.basic_items.edit_base_materials2(save_stats, ctx, bot)
					await mainmenu(ctx, save_stats)
				except Exception as e:
					await ctx.send("치명적인 오류발생! 관리자에게 이 메시지를 보여주세요.\n세이브 복구는 관리자가 해드립니다.\n불편을 드려 죄송합니다.```{}```".format(traceback.format_exc()))
					pass
					await mainmenu(ctx, save_stats)
			elif msg.content == "3":
				await ctx.send("설정할 가마토토 레벨을 입력하세요. (최대 120)")
				msg = await bot.wait_for('message', check=check)
				try:
					level = int(msg.content)
					if level >= 121:
						await ctx.send("120으로 설정됩니다.")
						level = 120
					edits.gamototo.gamatoto_xp.edit_gamatoto_xp2(save_stats, level)
					await ctx.send("세팅 완료: {}".format(level))
					await mainmenu(ctx, save_stats)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats)
			elif msg.content == "4":
				
				crew_data = edits.gamototo.helpers.get_helpers_send(save_stats)
				print(crew_data)
				await ctx.send("```1. 초보자: {}\n2. 초급: {}\n3. 중급: {}\n4. 카리스마: {}\n5. 레전드: {}```\n**총 대원수는 10명을 넘지 않아야 합니다!!**".format(crew_data['Intern'], crew_data['Lackey'], crew_data['Underling'], crew_data['Assistant'], crew_data['Legend']))
				msg = await bot.wait_for('message', check=check)
				if msg.content == "1":
					selected = 0
				elif msg.content == "2":
					selected = 1
				elif msg.content == "3":
					selected = 2
				elif msg.content == "4":
					selected = 3
				elif msg.content == "5":
					selected = 4
				else:
					await ctx.send("알 수 없는 옵션")
					pass
				
				try:
					await ctx.send("원하는 대원 수를 입력하세요.")
					msg = await bot.wait_for('message', check=check)
					try:
						count = int(msg.content)
						edits.gamototo.helpers.edit_helpers(save_stats, selected, count)
						await mainmenu(ctx, save_stats)
					except Exception as e:
						await ctx.send("치명적인 오류발생! 관리자에게 이 메시지를 보여주세요.\n세이브 복구는 관리자가 해드립니다.\n불편을 드려 죄송합니다.```{}```".format(traceback.format_exc()))
						pass
						await mainmenu(ctx, save_stats)

				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats)
			else:
			'''
			await mainmenu(ctx, save_stats, userid)
		elif msg.content == "4":
			await ctx.send("**BC Save Editor**\n```0. 뒤로가기\n1. 캐릭터 얻기\n2. 캐릭터 지우기\n3. 레벨링\n4. 3진```")
			msg = await bot.wait_for('message', check=check)
			if msg.content == "0":
				await mainmenu(ctx, save_stats, userid)
			elif msg.content == "1":
				await ctx.send("추가할 캐릭터의 아이디(3자리)를 입력해주세요.\n여러 캐릭터를 얻고 싶은 경우 띄어서 입력하세요.(예: 543 128 130)\n치트캐릭터를 제외하고 모두 얻고싶은 경우 all를 입력하세요.")
				msg = await bot.wait_for('message', check=check)
				if msg.content == "all":
					try:	
						
						cat_id = edits.cats.cat_id_selector.filter_obtainable_cats(save_stats, edits.cats.cat_id_selector.get_all_cats(save_stats))
						ids = helper.check_cat_ids(cat_id, save_stats)

						cats = save_stats["cats"]

						for cat_id in ids:
							cats[cat_id] = 1

						save_stats["cats"] = cats
						save_stats["menu_unlocks"][2] = 1
						await ctx.send("세팅 완료")
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				else:
					try:	
						#cat_id = int(msg.content)
						ids = user_input_handler.get_range(
							str(msg.content),
							length=len(save_stats["cats"]),
						)
						ids = helper.check_cat_ids(ids, save_stats)

						cats = save_stats["cats"]

						for cat_id in ids:
							cats[cat_id] = 1

						save_stats["cats"] = cats
						save_stats["menu_unlocks"][2] = 1
						await ctx.send("추가 완료")
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
			elif msg.content == "2":
				await ctx.send("제거할 캐릭터의 아이디(3자리)를 입력해주세요.\n여러 캐릭터를 제거하고 싶은 경우 띄어서 입력하세요.(예: 543 128 130)")
				msg = await bot.wait_for('message', check=check)
				try:	
					ids = user_input_handler.get_range(
						str(msg.content),
						length=len(save_stats["cats"]),
					)
					ids = helper.check_cat_ids(ids, save_stats)

					cats = save_stats["cats"]

					for cat_id in ids:
						cats[cat_id] = 0

					save_stats["cats"] = cats
					save_stats["menu_unlocks"][2] = 1
					
					await ctx.send("제거 완료")
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "3":
				await ctx.send("선택할 캐릭터의 아이디(3자리)를 입력해주세요.\n여러 캐릭터를 선택할 경우 띄어서 입력하세요.(예: 543 128 130)\n치트캐릭터를 제외하고 모두 선택할 경우 all를 입력하세요.\n현재 가지고있는 캐릭터를 모두 선택할 경우 unlocked를 입력하세요.")
				msg = await bot.wait_for('message', check=check)
				if msg.content == "all":
					try:	
						await ctx.send("레벨을 `기본레벨+플러스레벨` 형태로 입력하세요. (예: 60+70, 60+)")
						msg = await bot.wait_for('message', check=check)
						levels = str(msg.content)
						ids = edits.cats.cat_id_selector.filter_obtainable_cats(save_stats, edits.cats.cat_id_selector.get_all_cats(save_stats))
						#ds = helper.check_cat_ids(cat_id, save_stats)
						save_stats["cat_upgrades"] = edits.cats.upgrade_cats.upgrade_handler(
							data=save_stats["cat_upgrades"],
							ids=ids,
							level=levels,
							item_name="cat",
							save_stats=save_stats,
						)
						save_stats = edits.cats.upgrade_cats.set_user_popups(save_stats)
						save_stats = edits.cats.upgrade_cats.set_level_caps(save_stats)
						
						await ctx.send("세팅 완료")
						await mainmenu(ctx, save_stats, userid)
					except Exception as e:
						await ctx.send("치명적인 오류발생! 관리자에게 이 메시지를 보여주세요.\n세이브 복구는 관리자가 해드립니다.\n불편을 드려 죄송합니다.```{}```".format(traceback.format_exc()))
						pass
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "unlocked":
					try:	
						await ctx.send("레벨을 `기본레벨+플러스레벨` 형태로 입력하세요. (예: 60+70)")
						msg = await bot.wait_for('message', check=check)
						levels = str(msg.content)
						ids = edits.cats.cat_id_selector.select_current_cats(save_stats)
						#edits.cats.upgrade_cats.upgrade_cats_ids(save_stats, cat_id)
						save_stats["cat_upgrades"] = edits.cats.upgrade_cats.upgrade_handler(
							data=save_stats["cat_upgrades"],
							ids=ids,
							level=levels,
							item_name="cat",
							save_stats=save_stats,
						)
						save_stats = edits.cats.upgrade_cats.set_user_popups(save_stats)
						save_stats = edits.cats.upgrade_cats.set_level_caps(save_stats)

						
						await ctx.send("세팅 완료")
						await mainmenu(ctx, save_stats, userid)
					except Exception as e:
						await ctx.send("치명적인 오류발생! 관리자에게 이 메시지를 보여주세요.\n세이브 복구는 관리자가 해드립니다.\n불편을 드려 죄송합니다.```{}```".format(traceback.format_exc()))
						pass
						await mainmenu(ctx, save_stats, userid)
				else:
					try:	
						#cat_id = int(msg.content)
						
						ids = user_input_handler.get_range(
							str(msg.content),
							length=len(save_stats["cats"]),
						)
						await ctx.send("레벨을 `기본레벨+플러스레벨` 형태로 입력하세요. (예: 60+70, 60+ 등등)")
						msg = await bot.wait_for('message', check=check)
						levels = str(msg.content)
						save_stats["cat_upgrades"] = edits.cats.upgrade_cats.upgrade_handler(
							data=save_stats["cat_upgrades"],
							ids=ids,
							level=levels,
							item_name="cat",
							save_stats=save_stats,
						)
						save_stats = edits.cats.upgrade_cats.set_user_popups(save_stats)
						save_stats = edits.cats.upgrade_cats.set_level_caps(save_stats)
						#ids = helper.check_cat_ids(ids, save_stats)

						
						await ctx.send("세팅 완료")
						await mainmenu(ctx, save_stats, userid)
					except Exception as e:
						await ctx.send("치명적인 오류발생! 관리자에게 이 메시지를 보여주세요.\n세이브 복구는 관리자가 해드립니다.\n불편을 드려 죄송합니다.```{}```".format(traceback.format_exc()))
						pass
						await mainmenu(ctx, save_stats, userid)
			elif msg.content == "4":
				await ctx.send("3단 진화시킬 캐릭터의 아이디(3자리)를 입력해주세요.\n여러 캐릭터를 선택할 경우 띄어서 입력하세요.(예: 543 128 130)\n치트캐릭터를 제외하고 모두 선택할 경우 all를 입력하세요.\n현재 가지고있는 캐릭터를 모두 선택할 경우 unlocked를 입력하세요.")
				msg = await bot.wait_for('message', check=check)
				if msg.content == "all":
					try:	
						ids = edits.cats.cat_id_selector.filter_obtainable_cats(save_stats, edits.cats.cat_id_selector.get_all_cats(save_stats))
						edits.cats.evolve_cats.evolve_handler_ids(
							save_stats=save_stats,
							val=2,
							string="set",
							ids=ids,
							forced=False,
						)
						await ctx.send("세팅 완료")
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				elif msg.content == "unlocked":
					try:	
						
						ids = edits.cats.cat_id_selector.select_current_cats(save_stats)
						#edits.cats.upgrade_cats.upgrade_cats_ids(save_stats, cat_id)
						edits.cats.evolve_cats.evolve_handler_ids(
							save_stats=save_stats,
							val=2,
							string="set",
							ids=ids,
							forced=False,
						)
						
						await ctx.send("세팅 완료")
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
				else:
					try:	
						#cat_id = int(msg.content)
						
						ids = user_input_handler.get_range(
							str(msg.content),
							length=len(save_stats["cats"]),
						)
						edits.cats.evolve_cats.evolve_handler_ids(
							save_stats=save_stats,
							val=2,
							string="set",
							ids=ids,
							forced=False,
						)
						#ids = helper.check_cat_ids(ids, save_stats)

						
						await ctx.send("세팅 완료")
						await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
			else:
				await mainmenu(ctx, save_stats, userid)
		
		elif msg.content == "5":
			await ctx.send("**BC Save Editor**\n```0. 뒤로가기\n1. 메인스토리 클리어\n2. 보물\n3. 좀비 스테이지(사용불가)\n4. 구레전드 스테이지\n5. 신레전드 스테이지\n6. 마계의 문 잠금해제\n7. 마계편\n8. 탑(개발중)\n9. 필리버스터 스테이지 다시 플레이 가능하게 설정```")
			msg = await bot.wait_for('message', check=check)
			if msg.content == "0":
				await mainmenu(ctx, save_stats, userid)
			elif msg.content == "1":
				await ctx.send("**BC Save Editor**\n```0. 뒤로가기\n1. 세계편 1장까지\n2. 세계편 2장까지\n3. 세계편 3장까지\n4. 미래편 1장까지\n5. 미래편 2장까지\n6. 미래편 3장까지\n7. 우주편 1장까지\n8. 우주편 2장까지\n9. 우주편 3장까지```")
				msg = await bot.wait_for('message', check=check)
				try:
					if msg.content == "0":
						await mainmenu(ctx, save_stats, userid)
					elif msg.content == "1":
						levels_id = [0]
					elif msg.content == "2":
						levels_id = [0, 1]
					elif msg.content == "3":
						levels_id = [0, 1, 2]
					elif msg.content == "4":
						levels_id = [0, 1, 2, 3]
					elif msg.content == "5":
						levels_id = [0, 1, 2, 3, 4]
					elif msg.content == "6":
						levels_id = [0, 1, 2, 3, 4, 5]
					elif msg.content == "7":
						levels_id = [0, 1, 2, 3, 4, 5, 6]
					elif msg.content == "8":
						levels_id = [0, 1, 2, 3, 4, 5, 6, 7]
					elif msg.content == "9":
						levels_id = [0, 1, 2, 3, 4, 5, 6, 7, 8]
					#all id = [0, 1, 2, 3, 4, 5, 6, 7, 8]
					
					
					edits.levels.main_story.clear_all(save_stats, levels_id)
					await ctx.send("선택된 스테이지들을 클리어 하였습니다.")
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "2":
				await ctx.send("**BC Save Editor**\n```0. 뒤로가기\n1. 세계편 1장까지\n2. 세계편 2장까지\n3. 세계편 3장까지\n4. 미래편 1장까지\n5. 미래편 2장까지\n6. 미래편 3장까지\n7. 우주편 1장까지\n8. 우주편 2장까지\n9. 우주편 3장까지```")
				msg = await bot.wait_for('message', check=check)
				try:
					if msg.content == "0":
						await mainmenu(ctx, save_stats , userid)
					elif msg.content == "1":
						levels_id = [0]
					elif msg.content == "2":
						levels_id = [0, 1]
					elif msg.content == "3":
						levels_id = [0, 1, 2]
					elif msg.content == "4":
						levels_id = [0, 1, 2, 3]
					elif msg.content == "5":
						levels_id = [0, 1, 2, 3, 4]
					elif msg.content == "6":
						levels_id = [0, 1, 2, 3, 4, 5]
					elif msg.content == "7":
						levels_id = [0, 1, 2, 3, 4, 5, 6]
					elif msg.content == "8":
						levels_id = [0, 1, 2, 3, 4, 5, 6, 7]
					elif msg.content == "9":
						levels_id = [0, 1, 2, 3, 4, 5, 6, 7, 8]
					#all id = [0, 1, 2, 3, 4, 5, 6, 7, 8]
					
						
					
					await ctx.send("**BC Save Editor**\n```1. 조잡한 보물\n2. 평범한 보물\n3. 최고급 보물```")
					msg = await bot.wait_for('message', check=check)
					try:
						if msg.content == "1":
							tre_id = "1"
						elif msg.content == "2":
							tre_id = "2"
						elif msg.content == "3":
							tre_id = "3"
						else:
							await mainmenu(ctx, save_stats, userid)
						edits.levels.treasures.specific_stages_all_chapters(save_stats, levels_id, tre_id)
						await ctx.send("보물 세팅 완료되었습니다.")
						await mainmenu(ctx, save_stats, userid)
					except Exception as e:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await ctx.send("치명적인 오류발생! 관리자에게 이 메시지를 보여주세요.\n세이브 복구는 관리자가 해드립니다.\n불편을 드려 죄송합니다.```{}```".format(traceback.format_exc()))
						await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "3":
				try:
					await ctx.send("**BC Save Editor**\n```0. 뒤로가기\n1. 세계편 1장까지\n2. 세계편 2장까지\n3. 세계편 3장까지\n4. 미래편 1장까지\n5. 미래편 2장까지\n6. 미래편 3장까지\n7. 우주편 1장까지```")
					msg = await bot.wait_for('message', check=check)
					try:
						if msg.content == "0":
							await mainmenu(ctx, save_stats, userid)
						elif msg.content == "1":
							levels_id = [0]
						elif msg.content == "2":
							levels_id = [0, 1]
						elif msg.content == "3":
							levels_id = [0, 1, 2]
						elif msg.content == "4":
							levels_id = [0, 1, 2, 3]
						elif msg.content == "5":
							levels_id = [0, 1, 2, 3, 4]
						elif msg.content == "6":
							levels_id = [0, 1, 2, 3, 4, 5]
						elif msg.content == "7":
							levels_id = [0, 1, 2, 3, 4, 5, 6]
						
						#all id = [0, 1, 2, 3, 4, 5, 6, 7, 8]
						else:
							await mainmenu(ctx, save_stats, userid)
					except:
						await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
						await mainmenu(ctx, save_stats, userid)
					edits.levels.outbreaks.edit_outbreaks(save_stats, levels_id)
					await ctx.send("좀비 스테이지 완료되었습니다.")
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "4":
				try:
					await ctx.send("스테이지 장을 입력하세요.\n(전설의 시작: `1`)\n여러 장의 경우 (1장~49장: `1-49`)과 같이 입력하세요.\n모든 장의 경우 all를 입력하세요.")
					msg = await bot.wait_for('message', check=check)
					if msg.content == "all":
						stage_id = "all"
						await ctx.send("별 개수를 입력하세요. (1, 2, 3, 4)")
						msg = await bot.wait_for('message', check=check)
						star = str(msg.content)

					else:
						stage_id = str(msg.content)
						await ctx.send("별 개수를 입력하세요. (1, 2, 3, 4)")
						msg = await bot.wait_for('message', check=check)
						star = str(msg.content)

					edits.levels.event_stages.stories_of_legend(save_stats, stage_id, star)
					await ctx.send("구레전드 스테이지 클리어 완료")
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "5":
				try:
					await ctx.send("스테이지 장을 입력하세요.\n(고대의 저주: `1`)\n여러 장의 경우 (1장~49장: `1-49`)과 같이 입력하세요.\n모든 장의 경우 all를 입력하세요.")
					msg = await bot.wait_for('message', check=check)
					if msg.content == "all":
						stage_id = "all"
						await ctx.send("별 개수를 입력하세요. (1, 2, 3, 4)")
						msg = await bot.wait_for('message', check=check)
						star = str(msg.content)

					else:
						stage_id = str(msg.content)
						await ctx.send("별 개수를 입력하세요. (1, 2, 3, 4 중 하나 입력)")
						msg = await bot.wait_for('message', check=check)
						star = str(msg.content)

					edits.levels.uncanny.edit_uncanny(save_stats, stage_id, star)
					await ctx.send("신레전드 스테이지 클리어 완료")
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "6":
				try:
					edits.levels.unlock_aku_realm.unlock_aku_realm(save_stats)
					await ctx.send("마계의 문 오픈 완료")
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "7":#마계편
				try:
					await ctx.send("스테이지 ID를 입력하세요. (모두: 49, 1스테이지: 1)")
					msg = await bot.wait_for('message', check=check)
					aku_stage = str(msg.content)
					edits.levels.aku.edit_aku(save_stats, aku_stage)
					await ctx.send("마계편 스테이지 클리어 완료")
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "8":#탑
				try:
					await ctx.send("developing")
					await mainmenu(ctx, save_stats, userid)
					'''
					await ctx.send("스테이지 ID를 입력하세요. (모두: 49, 1스테이지: 1)")
					msg = await bot.wait_for('message', check=check)
					edits.levels.towers.edit_tower(save_stats)
					await ctx.send("마계편 스테이지 클리어 완료")
					await mainmenu(ctx, save_stats)
					'''
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "9":
				try:
					edits.levels.allow_filibuster_clearing.allow_filibuster_clearing(save_stats)
					await ctx.send("재설정 완료. 이제 필리버스터 스테이지를 다시 플레이할 수 있습니다.")
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			else:
				await mainmenu(ctx, save_stats, userid)
			
			
		elif msg.content == "6":
			await ctx.send("**BC Save Editor**\n```0. 뒤로가기\n1. 트래커리셋 / 문의코드 재생성 / 토큰 초기화\n2.```")
			msg = await bot.wait_for('message', check=check)
			if msg.content == "0":
				await mainmenu(ctx, save_stats, userid)
			elif msg.content == "1":
				try:
					edits.other.create_new_account.create_new_account(save_stats)
					await ctx.send("트래커 리셋, 문의코드 재생성, 토큰 초기화 완료되었습니다.")
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			else:
				await mainmenu(ctx, save_stats, userid)
		elif msg.content == "7":
			await ctx.send("**BC Save Editor**\n```0. 뒤로가기\n1. 골드패스 얻기\n2. 뽑기 시드 확인&변경\n3. 플레이타임 설정\n4. 적 도감 모두 잠금해제\n5. ```")
			msg = await bot.wait_for('message', check=check)
			if msg.content == "0":
				await mainmenu(ctx, save_stats, userid)
			elif msg.content == "1":
				try:	
					#print(save_stats["gold_pass"])
					edits.other.get_gold_pass.get_gold_pass(save_stats)

					#await ctx.send("세팅 완료: {}".format(cat_id))
					await ctx.send("골드패스 세팅 완료.")
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "2":
				try:	
					await ctx.send("현재 레어 뽑기 시드: {}\n변경될 원하는 시드 번호를 정확히 입력하세요.\n변경을 원하지 않을 경우, 그대로 입력하세요.\n잘못 건드리면 뽑기가 불가능할 수 있습니다.".format(save_stats["rare_gacha_seed"]["Value"]))
					msg = await bot.wait_for('message', check=check)
					value = int(msg.content)
					save_stats["rare_gacha_seed"]["Value"] = value
					await ctx.send("시드 변경완료: {}".format(value))
					
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "3":
				try:	
					
					play_time = save_stats["play_time"]
					await ctx.send("현재 플레이타임: {}시간 {}분\n변경할 시간과 분을 `<시간>:<분>` 형식으로 입력하세요. (예: 123:45)".format(play_time["hh"], play_time["mm"]))
					msg = await bot.wait_for('message', check=check)
					plset = msg.content.split(":")
					hourset = int(plset[0])
					minset = int(plset[1])
					play_time["hh"] = hourset
					play_time["mm"] = minset
					await ctx.send("플레이타임 변경완료: {}시간 {}분".format(hourset, minset))
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "4":
				try:	
					edits.other.unlock_enemy_guide.enemy_guide(save_stats)
					await ctx.send("적 도감을 모두 잠금해제하였습니다.")
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
			elif msg.content == "5":
				try:	
					await ctx.send("```1. XP기부\n2. 레벨```")
					msg = await bot.wait_for('message', check=check)
					if msg.content == "1":
						edits.other.cat_shrine.edit_shrine_xp2(save_stats)
					elif msg.content == "2":
						edits.other.cat_shrine.edit_shrine_xp(save_stats)
					await mainmenu(ctx, save_stats, userid)
				except:
					await ctx.send("알 수 없는 오류\n메인메뉴로 돌아갑니다.")
					await mainmenu(ctx, save_stats, userid)
					
			else:
				await mainmenu(ctx, save_stats, userid)
		else:
			await mainmenu(ctx, save_stats, userid)







@bot.event
async def on_ready():
	await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="BCSFE Bot by PULSE"))
	print("Bot is ready!")
    
    
bot.run("")
