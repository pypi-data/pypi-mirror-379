import asyncio
import base64
import platform
import re
import os
from io import BytesIO
from typing import List, Optional, Tuple
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from nonebot import logger, get_plugin_config
from .get_motd import ServerStatus, get_summary_stats
from .config import Config

# 获取配置
plugin_config = get_plugin_config(Config)


class ServerListDrawer:
    def __init__(self):
        # 基础配置 - 从配置文件读取
        self.width = plugin_config.mc_motd_image_width
        self.margin = plugin_config.mc_motd_margin
        self.item_height = plugin_config.mc_motd_item_height
        self.header_height = 120
        self.footer_height = 60
        self.corner_radius = 16
        self.shadow_offset = 4
        
        # 项目间距配置
        self.item_spacing = 20
        self.detail_extra_height = 80

        # 颜色配置 - 深色主题
        self.colors = {
            'background': '#0d1117',
            'background_secondary': '#161b22',
            'card_bg': '#21262d',
            'card_bg_hover': '#30363d',
            'header_bg': '#1c2128',
            'online_accent': '#238636',
            'online_light': '#2ea043',
            'offline_accent': '#da3633',
            'offline_light': '#f85149',
            'warning_accent': '#d29922',
            'warning_light': '#f0883e',
            'primary_text': '#f0f6fc',
            'secondary_text': '#8b949e',
            'muted_text': '#6e7681',
            'accent_blue': '#58a6ff',
            'accent_purple': '#bc8cff',
            'divider': '#21262d',
            'shadow': '#000000',
            'gradient_start': '#1c2128',
            'gradient_end': '#0d1117',
            'bot_accent': '#fd7e14',
        }

        # 初始化字体
        self._init_fonts()

    def _init_fonts(self):
        try:
            # 定义不同字体大小
            font_sizes = {
                'title': 32,
                'large': 22,
                'medium': 18,
                'small': 15,
                'tiny': 13
            }

            # 优先使用自定义字体
            custom_font_name = plugin_config.mc_motd_custom_font.strip()
            if custom_font_name:
                # 支持多种扩展名
                font_extensions = ['.ttf', '.otf', '.ttc']
                custom_font_path = None
                
                for ext in font_extensions:
                    test_path = f"data/fonts/{custom_font_name}{ext}"
                    if os.path.exists(test_path):
                        custom_font_path = test_path
                        break
                
                if custom_font_path:
                    try:
                        # 测试字体是否可以正常加载
                        test_font = ImageFont.truetype(custom_font_path, font_sizes['medium'])
                        
                        # 如果测试成功，为所有尺寸创建字体
                        self.fonts = {}
                        for size_name, size in font_sizes.items():
                            self.fonts[size_name] = ImageFont.truetype(custom_font_path, size)
                        
                        logger.success(f"成功加载自定义字体: {custom_font_path}")
                        return
                        
                    except Exception as e:
                        logger.error(f"自定义字体加载失败: {e}")
                else:
                    logger.warning(f"自定义字体文件不存在: data/fonts/{custom_font_name}[.ttf/.otf/.ttc]")

            # 使用系统字体作为备用
            logger.info("使用系统字体")
            
            system = platform.system()
            logger.info(f"检测到操作系统: {system}")

            # 根据操作系统选择字体
            fonts_to_try = []

            if system == "Windows":
                fonts_to_try = [
                    "C:/Windows/Fonts/msyhbd.ttc",
                    "C:/Windows/Fonts/msyh.ttc",
                    "C:/Windows/Fonts/simhei.ttf",
                    "C:/Windows/Fonts/simsun.ttc",
                    "msyh.ttc",
                    "simhei.ttf",
                ]
            elif system == "Darwin":
                fonts_to_try = [
                    "/System/Library/Fonts/PingFang.ttc",
                    "/System/Library/Fonts/STHeiti Medium.ttc",
                    "PingFang SC",
                    "STHeiti",
                ]
            else:
                fonts_to_try = [
                    "/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf",
                    "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
                    "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
                    "WenQuanYi Zen Hei",
                    "DejaVu Sans",
                ]

            # 尝试加载字体
            self.fonts = {}
            font_loaded = False

            for font_path in fonts_to_try:
                try:
                    test_font = ImageFont.truetype(font_path, font_sizes['medium'])

                    for size_name, size in font_sizes.items():
                        self.fonts[size_name] = ImageFont.truetype(font_path, size)

                    logger.success(f"成功加载系统字体: {font_path}")
                    font_loaded = True
                    break

                except (OSError, IOError):
                    continue

            if not font_loaded:
                logger.warning("使用默认字体")
                for size_name in font_sizes:
                    self.fonts[size_name] = ImageFont.load_default()

        except Exception as e:
            logger.error(f"字体初始化失败: {e}")
            default_font = ImageFont.load_default()
            self.fonts = {name: default_font for name in ['title', 'large', 'medium', 'small', 'tiny']}

    def clean_text_for_display(self, text: str) -> str:
        if not text:
            return ""

        # 移除emoji和其他Unicode符号，保留基本的ASCII字符、中文字符和常用标点
        cleaned = re.sub(r'[^\u4e00-\u9fff\u3400-\u4dbf\w\s\.\-_:\/\[\]()（）、，。！？""'']+', '', text)
        
        # 清理多余的空格
        cleaned = re.sub(r'\s+', ' ', cleaned).strip()

        return cleaned

    def create_gradient_background(self, width: int, height: int) -> Image.Image:
        gradient = Image.new('RGB', (width, height), self.colors['background'])
        draw = ImageDraw.Draw(gradient)

        # 从上到下的渐变
        for y in range(height):
            ratio = y / height
            start_color = tuple(int(self.colors['gradient_start'][i:i + 2], 16) for i in (1, 3, 5))
            end_color = tuple(int(self.colors['gradient_end'][i:i + 2], 16) for i in (1, 3, 5))
            color = tuple(int(start_color[i] + (end_color[i] - start_color[i]) * ratio) for i in range(3))
            draw.line([(0, y), (width, y)], fill=color)

        return gradient

    def draw_rounded_rectangle(self, draw: ImageDraw.Draw, bbox: tuple, radius: int, fill: str):
        x1, y1, x2, y2 = bbox
        radius = min(radius, (x2 - x1) // 2, (y2 - y1) // 2)

        # 绘制主体矩形
        draw.rectangle([x1 + radius, y1, x2 - radius, y2], fill=fill)
        draw.rectangle([x1, y1 + radius, x2, y2 - radius], fill=fill)

        # 绘制四个角的圆形
        draw.pieslice([x1, y1, x1 + 2 * radius, y1 + 2 * radius], 180, 270, fill=fill)
        draw.pieslice([x2 - 2 * radius, y1, x2, y1 + 2 * radius], 270, 360, fill=fill)
        draw.pieslice([x1, y2 - 2 * radius, x1 + 2 * radius, y2], 90, 180, fill=fill)
        draw.pieslice([x2 - 2 * radius, y2 - 2 * radius, x2, y2], 0, 90, fill=fill)

    def draw_rounded_rectangle_with_shadow(self, draw: ImageDraw.Draw, bbox: tuple,
                                           radius: int, fill: str, shadow_color: str = None):
        x1, y1, x2, y2 = bbox

        # 绘制阴影
        if shadow_color:
            shadow_bbox = (x1 + self.shadow_offset, y1 + self.shadow_offset,
                           x2 + self.shadow_offset, y2 + self.shadow_offset)
            self.draw_rounded_rectangle(draw, shadow_bbox, radius, shadow_color)

        # 绘制主体
        self.draw_rounded_rectangle(draw, bbox, radius, fill)

    def safe_text_draw(self, draw: ImageDraw.Draw, position: tuple, text: str,
                       font: ImageFont.ImageFont, fill: str, fallback_text: str = None):
        try:
            clean_text = self.clean_text_for_display(text)
            if clean_text:
                draw.text(position, clean_text, font=font, fill=fill)
            elif fallback_text:
                draw.text(position, fallback_text, font=font, fill=fill)
        except Exception as e:
            logger.warning(f"绘制文本失败: {e}")
            if fallback_text:
                try:
                    draw.text(position, fallback_text, font=font, fill=fill)
                except:
                    draw.text(position, "[TEXT ERROR]", font=font, fill=fill)

    def create_status_badge(self, is_online: bool, size: Tuple[int, int] = (80, 24)) -> Image.Image:
        width, height = size
        badge = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        draw = ImageDraw.Draw(badge)

        # 选择颜色
        if is_online:
            bg_color = self.colors['online_accent']
            text_color = '#ffffff'
            text = '在线'
        else:
            bg_color = self.colors['offline_accent']
            text_color = '#ffffff'
            text = '离线'

        # 绘制徽章背景
        self.draw_rounded_rectangle(draw, (0, 0, width, height), height // 2, bg_color)

        # 绘制文本
        try:
            text_bbox = draw.textbbox((0, 0), text, font=self.fonts['tiny'])
            text_width = text_bbox[2] - text_bbox[0]
            text_height = text_bbox[3] - text_bbox[1]
            text_x = (width - text_width) // 2
            text_y = (height - text_height) // 2
            self.safe_text_draw(draw, (text_x, text_y), text, self.fonts['tiny'], text_color)
        except:
            # 如果文本绘制失败，绘制状态点
            dot_size = 8
            dot_x = (width - dot_size) // 2
            dot_y = (height - dot_size) // 2
            draw.ellipse([dot_x, dot_y, dot_x + dot_size, dot_y + dot_size], fill=text_color)

        return badge

    def parse_server_icon(self, icon_data: str) -> Optional[Image.Image]:
        try:
            if not icon_data or not icon_data.startswith('data:image'):
                return None

            header, data = icon_data.split(',', 1)
            icon_bytes = base64.b64decode(data)
            icon = Image.open(BytesIO(icon_bytes))
            icon = icon.resize((72, 72), Image.Resampling.LANCZOS)

            if icon.mode != 'RGBA':
                icon = icon.convert('RGBA')

            return icon
        except Exception as e:
            logger.warning(f"解析服务器图标失败: {e}")
            return None

    def create_default_icon(self, is_online: bool = True) -> Image.Image:
        icon = Image.new('RGBA', (72, 72), (0, 0, 0, 0))
        draw = ImageDraw.Draw(icon)

        if is_online:
            bg_color = self.colors['online_accent']
            accent_color = self.colors['online_light']
        else:
            bg_color = self.colors['offline_accent']
            accent_color = self.colors['offline_light']

        # 绘制圆角背景
        self.draw_rounded_rectangle(draw, (8, 8, 64, 64), 12, bg_color)

        # 绘制装饰图案
        draw.rectangle([20, 20, 32, 32], fill=accent_color)
        draw.rectangle([36, 20, 48, 32], fill=accent_color)
        draw.rectangle([20, 36, 32, 48], fill=accent_color)
        draw.rectangle([36, 36, 48, 48], fill=accent_color)

        return icon

    def draw_header(self, draw: ImageDraw.Draw, stats: dict):
        # 绘制标题背景
        header_rect = (0, 0, self.width, self.header_height)
        self.draw_rounded_rectangle_with_shadow(draw, header_rect, self.corner_radius,
                                                self.colors['header_bg'],
                                                self.colors['shadow'] + '40')

        # 主标题 - 使用配置中的标题
        title = plugin_config.mc_motd_title
        try:
            title_bbox = draw.textbbox((0, 0), title, font=self.fonts['title'])
            title_width = title_bbox[2] - title_bbox[0]
            title_x = (self.width - title_width) // 2
            self.safe_text_draw(draw, (title_x, 25), title, self.fonts['title'],
                                self.colors['primary_text'], "Minecraft Server Status")
        except:
            self.safe_text_draw(draw, (self.width // 2 - 150, 25), "Minecraft Server Status",
                                self.fonts['title'], self.colors['primary_text'])

        # 统计信息 - 修改为：玩家n 假人n 合计n
        stats_parts = []
        if stats['total'] > 0:
            # 计算真实玩家数和假人数
            real_players = stats['total_players']
            total_bots = stats.get('bots_filtered', 0)
            total_combined = real_players + total_bots
            
            stats_parts.append(f"玩家 {real_players}")
            if plugin_config.mc_motd_filter_bots and total_bots > 0:
                stats_parts.append(f"假人 {total_bots}")
            stats_parts.append(f"合计 {total_combined}")
            
            if stats.get('average_latency'):
                stats_parts.append(f"平均延迟 {stats['average_latency']}ms")

        if stats_parts:
            stats_text = " | ".join(stats_parts)
            try:
                stats_bbox = draw.textbbox((0, 0), stats_text, font=self.fonts['small'])
                stats_width = stats_bbox[2] - stats_bbox[0]
                stats_x = (self.width - stats_width) // 2
                self.safe_text_draw(draw, (stats_x, 75), stats_text, self.fonts['small'],
                                    self.colors['secondary_text'])
            except:
                simple_stats = f"Players: {stats['total_players']} | Total: {stats['total_players'] + stats.get('bots_filtered', 0)}"
                self.safe_text_draw(draw, (self.width // 2 - 100, 75), simple_stats,
                                    self.fonts['small'], self.colors['secondary_text'])

    def draw_server_item(self, draw: ImageDraw.Draw, image: Image.Image,
                         y: int, status: ServerStatus, index: int, show_detail: bool = False):
        item_height = self.item_height
        if show_detail and status.is_online and status.players_list_filtered:
            item_height += self.detail_extra_height

        item_rect = (self.margin, y, self.width - self.margin, y + item_height)

        # 绘制卡片背景（带阴影）
        self.draw_rounded_rectangle_with_shadow(draw, item_rect, self.corner_radius,
                                                self.colors['card_bg'],
                                                self.colors['shadow'] + '30')

        # 绘制左侧状态指示条
        status_color = self.colors['online_accent'] if status.is_online else self.colors['offline_accent']
        status_rect = (self.margin, y, self.margin + 6, y + item_height)
        self.draw_rounded_rectangle(draw, status_rect, 3, status_color)

        # 绘制服务器图标
        icon_x = self.margin + 25
        icon_y = y + 25

        # 获取或创建图标
        icon = None
        if status.icon:
            icon = self.parse_server_icon(status.icon)

        if not icon:
            icon = self.create_default_icon(status.is_online)

        # 粘贴图标
        try:
            image.paste(icon, (icon_x, icon_y), icon)
        except Exception as e:
            logger.warning(f"粘贴图标失败: {e}")

        # 文字区域
        text_x = icon_x + 90

        # 服务器名称
        name_text = status.tag
        if len(name_text) > 25:
            name_text = name_text[:22] + "..."
        self.safe_text_draw(draw, (text_x, y + 20), name_text, self.fonts['large'],
                            self.colors['primary_text'], f"Server {index + 1}")

        # 服务器地址
        self.safe_text_draw(draw, (text_x, y + 50), status.ip_port, self.fonts['medium'],
                            self.colors['secondary_text'])

        # 右侧状态徽章
        badge_x = self.width - self.margin - 90
        badge_y = y + 20
        status_badge = self.create_status_badge(status.is_online)
        try:
            image.paste(status_badge, (badge_x, badge_y), status_badge)
        except Exception as e:
            logger.warning(f"粘贴状态徽章失败: {e}")

        # 状态信息
        status_y = y + 80

        if status.is_online:
            status_info = []

            # 延迟信息
            if status.latency:
                status_info.append(f"延迟 {status.latency}ms")

            # 玩家信息
            if status.players_online is not None:
                player_text = f"玩家 {status.players_online}/{status.players_max or '?'}"
                status_info.append(player_text)

            if status_info:
                status_text = " | ".join(status_info)
                self.safe_text_draw(draw, (text_x, status_y), status_text, self.fonts['small'],
                                    self.colors['online_accent'])

            # MOTD信息
            if status.motd_clean:
                motd_text = self.clean_text_for_display(status.motd_clean)
                if len(motd_text) > 70:
                    motd_text = motd_text[:67] + "..."
                if motd_text:
                    self.safe_text_draw(draw, (text_x, y + 105), f"MOTD: {motd_text}",
                                        self.fonts['tiny'], self.colors['muted_text'])

            # 详细模式：显示玩家列表
            if show_detail and status.players_list_filtered:
                players_y = y + 130
                
                # 玩家列表标题
                self.safe_text_draw(draw, (text_x, players_y), "在线玩家:",
                                    self.fonts['small'], self.colors['accent_blue'])
                
                # 玩家名称列表
                players_per_line = 6
                player_lines = []
                current_line = []
                
                for i, player in enumerate(status.players_list_filtered[:30]):
                    current_line.append(player)
                    if len(current_line) >= players_per_line or i == len(status.players_list_filtered) - 1:
                        player_lines.append(", ".join(current_line))
                        current_line = []
                
                for i, line in enumerate(player_lines[:3]):
                    self.safe_text_draw(draw, (text_x + 20, players_y + 25 + i * 20), line,
                                        self.fonts['tiny'], self.colors['secondary_text'])
                
                # 如果玩家太多，显示省略号
                if len(status.players_list_filtered) > 30:
                    self.safe_text_draw(draw, (text_x + 20, players_y + 85), 
                                        f"... 等{len(status.players_list_filtered)}名玩家",
                                        self.fonts['tiny'], self.colors['muted_text'])
                
                # 假人过滤信息
                if plugin_config.mc_motd_filter_bots and len(status.players_list_filtered) < len(status.players_list or []):
                    bot_count = len(status.players_list) - len(status.players_list_filtered)
                    self.safe_text_draw(draw, (self.width - self.margin - 200, players_y + 25), 
                                        f"已过滤假人: {bot_count}个",
                                        self.fonts['tiny'], self.colors['bot_accent'])

        else:
            # 离线状态
            offline_text = "离线"
            if status.error_message:
                error_msg = self.clean_text_for_display(status.error_message)
                if len(error_msg) > 35:
                    error_msg = error_msg[:32] + "..."
                if error_msg:
                    offline_text += f" | {error_msg}"

            self.safe_text_draw(draw, (text_x, status_y), offline_text, self.fonts['small'],
                                self.colors['offline_accent'])

        # 版本信息（右下角）
        if status.version and status.is_online:
            version_text = self.clean_text_for_display(status.version)
            if version_text and len(version_text) > 0:
                try:
                    version_bbox = draw.textbbox((0, 0), version_text, font=self.fonts['tiny'])
                    version_width = version_bbox[2] - version_bbox[0]
                    version_x = self.width - self.margin - version_width - 20
                    version_y = y + item_height - 30
                    self.safe_text_draw(draw, (version_x, version_y), version_text,
                                        self.fonts['tiny'], self.colors['muted_text'])
                except Exception as e:
                    logger.warning(f"绘制版本信息失败: {e}")

        return item_height

    def draw_footer(self, draw: ImageDraw.Draw, y: int):
        footer_text = "Powered by NoneBot MC MOTD Plugin"
        try:
            footer_bbox = draw.textbbox((0, 0), footer_text, font=self.fonts['tiny'])
            footer_width = footer_bbox[2] - footer_bbox[0]
            footer_x = (self.width - footer_width) // 2
            self.safe_text_draw(draw, (footer_x, y + 25), footer_text, self.fonts['tiny'],
                                self.colors['muted_text'])
        except:
            self.safe_text_draw(draw, (self.width // 2 - 120, y + 25), "NoneBot Plugin",
                                self.fonts['tiny'], self.colors['muted_text'])

    def create_empty_state_image(self) -> bytes:
        height = 400

        # 创建渐变背景
        image = self.create_gradient_background(self.width, height)
        draw = ImageDraw.Draw(image)

        # 绘制空状态卡片
        card_rect = (self.margin * 2, height // 2 - 80, self.width - self.margin * 2, height // 2 + 80)
        self.draw_rounded_rectangle_with_shadow(draw, card_rect, self.corner_radius,
                                                self.colors['card_bg'],
                                                self.colors['shadow'] + '40')

        # 空状态文本
        empty_text = "还没有添加任何服务器"
        help_text = "管理员可使用 /motd add ip:port 标签 来添加服务器"

        try:
            empty_bbox = draw.textbbox((0, 0), empty_text, font=self.fonts['large'])
            empty_width = empty_bbox[2] - empty_bbox[0]
            empty_x = (self.width - empty_width) // 2

            help_bbox = draw.textbbox((0, 0), help_text, font=self.fonts['medium'])
            help_width = help_bbox[2] - help_bbox[0]
            help_x = (self.width - help_width) // 2

            self.safe_text_draw(draw, (empty_x, height // 2 - 30), empty_text,
                                self.fonts['large'], self.colors['primary_text'])
            self.safe_text_draw(draw, (help_x, height // 2 + 10), help_text,
                                self.fonts['medium'], self.colors['secondary_text'])
        except:
            self.safe_text_draw(draw, (self.width // 2 - 100, height // 2 - 20), "No servers added",
                                self.fonts['large'], self.colors['primary_text'])
            self.safe_text_draw(draw, (self.width // 2 - 120, height // 2 + 10), "Use /motd add ip:port tag",
                                self.fonts['medium'], self.colors['secondary_text'])

        buffer = BytesIO()
        image.save(buffer, format='PNG', quality=95)
        return buffer.getvalue()

    async def draw_server_list(self, server_statuses: List[ServerStatus], show_detail: bool = False) -> Optional[bytes]:
        try:
            if not server_statuses:
                logger.info("没有服务器数据，生成空状态图片")
                return self.create_empty_state_image()

            # 计算每个服务器项的实际高度（考虑详细模式）
            item_heights = []
            total_content_height = 0
            
            for status in server_statuses:
                base_height = self.item_height
                if show_detail and status.is_online and status.players_list_filtered:
                    base_height += self.detail_extra_height
                item_heights.append(base_height)
                total_content_height += base_height + self.item_spacing

            # 移除最后一个间距
            if item_heights:
                total_content_height -= self.item_spacing

            # 计算图片总高度
            total_height = (self.header_height + total_content_height +
                            self.footer_height + self.margin * 4)

            # 创建渐变背景
            image = self.create_gradient_background(self.width, total_height)
            draw = ImageDraw.Draw(image)

            # 计算统计信息
            stats = get_summary_stats(server_statuses)

            # 绘制标题
            self.draw_header(draw, stats)

            # 绘制服务器列表
            current_y = self.header_height + self.margin * 2
            for index, status in enumerate(server_statuses):
                item_height = self.draw_server_item(draw, image, current_y, status, index, show_detail)
                current_y += item_height + self.item_spacing

            # 绘制底部
            self.draw_footer(draw, current_y + self.margin - self.item_spacing)

            # 转换为字节数据
            buffer = BytesIO()
            image.save(buffer, format='PNG', quality=95, optimize=True)
            image_bytes = buffer.getvalue()
            buffer.close()

            mode_text = "详细模式" if show_detail else "普通模式"
            logger.success(f"成功生成服务器列表图片（{mode_text}），大小: {len(image_bytes)} bytes")
            return image_bytes

        except Exception as e:
            logger.error(f"绘制服务器列表时发生错误: {e}")
            return None


# 创建全局绘图器实例
drawer = ServerListDrawer()


# 提供简单的函数接口
async def draw_server_list(server_statuses: List[ServerStatus], show_detail: bool = False) -> Optional[bytes]:
    return await drawer.draw_server_list(server_statuses, show_detail)